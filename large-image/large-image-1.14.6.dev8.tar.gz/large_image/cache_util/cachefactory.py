#############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#############################################################################

import math
import threading

import cachetools

try:
    import psutil
except ImportError:
    psutil = None

try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points

from .. import config
from ..exceptions import TileCacheError

try:
    from .memcache import MemCache
except ImportError:
    MemCache = None

# DO NOT MANUALLY ADD ANYTHING TO `_availableCaches`
#  use entrypoints and let loadCaches fill in `_availableCaches`
_availableCaches = {}


def loadCaches(entryPointName='large_image.cache', sourceDict=_availableCaches):
    """
    Load all caches from entrypoints and add them to the
    availableCaches dictionary.

    :param entryPointName: the name of the entry points to load.
    :param sourceDict: a dictionary to populate with the loaded caches.
    """
    if len(_availableCaches):
        return
    epoints = entry_points()
    if entryPointName in epoints:
        for entryPoint in epoints[entryPointName]:
            try:
                cacheClass = entryPoint.load()
                sourceDict[entryPoint.name.lower()] = cacheClass
                config.getConfig('logprint').debug(f'Loaded cache {entryPoint.name}')
            except Exception:
                config.getConfig('logprint').exception(
                    f'Failed to load cache {entryPoint.name}'
                )
    # Load memcached last for now
    if MemCache is not None:
        # TODO: put this in an entry point for a new package
        _availableCaches['memcached'] = MemCache
    # NOTE: `python` cache is viewed as a fallback and isn't listed in `availableCaches`


def pickAvailableCache(sizeEach, portion=8, maxItems=None, cacheName=None):
    """
    Given an estimated size of an item, return how many of those items would
    fit in a fixed portion of the available virtual memory.

    :param sizeEach: the expected size of an item that could be cached.
    :param portion: the inverse fraction of the memory which can be used.
    :param maxItems: if specified, the number of items is never more than this
        value.
    :param cacheName: if specified, the portion can be affected by the
        configuration.
    :return: the number of items that should be cached.  Always at least two,
        unless maxItems is less.
    """
    if cacheName:
        portion = max(portion, int(config.getConfig(
            f'cache_{cacheName}_memory_portion', portion)))
        configMaxItems = int(config.getConfig(f'cache_{cacheName}_maximum', 0))
        if configMaxItems > 0:
            maxItems = configMaxItems
    # Estimate usage based on (1 / portion) of the total virtual memory.
    if psutil:
        memory = psutil.virtual_memory().total
    else:
        memory = 1024 ** 3
    numItems = max(int(math.floor(memory / portion / sizeEach)), 2)
    if maxItems:
        numItems = min(numItems, maxItems)
    return numItems


def getFirstAvailableCache():
    cacheBackend = config.getConfig('cache_backend', None)
    if cacheBackend is not None:
        raise ValueError('cache_backend already set')
    loadCaches()
    cache, cacheLock = None, None
    for cacheBackend in _availableCaches:
        try:
            cache, cacheLock = _availableCaches[cacheBackend].getCache()
            break
        except TileCacheError:
            continue
    if cache is not None:
        config.getConfig('logprint').info(
            f'Automatically setting `{cacheBackend}` as cache_backend from availableCaches'
        )
        config.setConfig('cache_backend', cacheBackend)
    return cache, cacheLock


class CacheFactory:
    logged = False

    def getCacheSize(self, numItems, cacheName=None):
        if numItems is None:
            defaultPortion = 32
            try:
                portion = int(config.getConfig('cache_python_memory_portion', 0))
                if cacheName:
                    portion = max(portion, int(config.getConfig(
                        f'cache_{cacheName}_memory_portion', portion)))
                portion = max(portion or defaultPortion, 3)
            except ValueError:
                portion = defaultPortion
            numItems = pickAvailableCache(256**2 * 4 * 2, portion)
        if cacheName:
            try:
                maxItems = int(config.getConfig(f'cache_{cacheName}_maximum', 0))
                if maxItems > 0:
                    numItems = min(numItems, max(maxItems, 3))
            except ValueError:
                pass
        return numItems

    def getCache(self, numItems=None, cacheName=None, inProcess=False):
        loadCaches()

        # Default to `python` cache for inProcess
        cacheBackend = config.getConfig('cache_backend', 'python' if inProcess else None)

        if isinstance(cacheBackend, str):
            cacheBackend = cacheBackend.lower()

        cache = None
        if not inProcess and cacheBackend in _availableCaches:
            cache, cacheLock = _availableCaches[cacheBackend].getCache()
        elif not inProcess and cacheBackend is None:
            cache, cacheLock = getFirstAvailableCache()

        if cache is None:  # fallback backend or inProcess
            cacheBackend = 'python'
            cache = cachetools.LRUCache(self.getCacheSize(numItems, cacheName=cacheName))
            cacheLock = threading.Lock()

        if not inProcess and not CacheFactory.logged:
            config.getConfig('logprint').info(f'Using {cacheBackend} for large_image caching')
            CacheFactory.logged = True

        return cache, cacheLock
