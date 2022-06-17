from ..core.helpers import itemize, splitModRef, normpath, expandDir
from .repo import checkoutRepo
from .links import provenanceLink


# GET DATA FOR MAIN SOURCE AND ALL MODULES


class AppData(object):
    def __init__(
        self, app, host, moduleRefs, locations, modules, version, checkout, silent
    ):
        """Collects TF data according to specifications.

        The specifications are passed as arguments when the object is initialized.

        Parameters
        ----------
        host: string, optional None
            If present, it points to a GitLab instance such as the on-premise
            `gitlab.huc.knaw.nl` or the public `gitlab.com`.
            If `None` we work with `github.com`.
        app: obj
            The high-level API object
        moduleRefs: tuple
            Each member consists of a module ref, which is a tuple of information
            that defines a module.
        locations: string|tuple
            One or more directory paths. They will be combined with the `modules`
            argument and used as locations to search for TF data files.
        modules: string|tuple
            One or more directory path segments. They will be appended to the
            paths given by the `locations` argument to form search locations
            for TF data files.
        version: string
            The version of TF data that should be retrievend. Version is a directory
            level just below the search locations.
        checkout: string
            A specifier to use a specific release or commit of a data repository.
        silent:
            The desired verbosity when reporting on the progress and result of the
            data fetching.

        """
        self.host = host
        self.app = app
        self.moduleRefs = (
            []
            if moduleRefs is None
            else moduleRefs.split(",")
            if type(moduleRefs) is str
            else list(moduleRefs)
        )
        self.locationsArg = locations
        self.modulesArg = modules
        self.version = version
        self.checkout = checkout
        self.silent = silent

    def getMain(self):
        """Get the main data of the corpus.

        This is specified by the `org`, `repo` and `relative` settings under
        `provenanceSpec` in `config.yaml`.

        See Also
        --------
        tf.advanced.settings: options allowed in `config.yaml`
        """

        app = self.app
        aContext = app.context
        org = aContext.org
        repo = aContext.repo
        relative = aContext.relative
        appPath = aContext.appPath
        appName = aContext.appName

        if appName.startswith("app:"):
            appParent = appPath.rsplit("/", 1)[0]
            relative = f"{appParent}/{relative}"
        elif org is None or repo is None:
            appPathRep = f"{appPath}/" if appPath else ""
            relative = f"{appPathRep}{appName}"
            self.checkout = "local"

        if not self.getModule(org, repo, relative, self.checkout, isBase=True):
            self.good = False

    def getStandard(self):
        """Get the data of the standard modules specified by the settings of the corpus.

        These are specified in the `moduleSpecs` setting under
        `provenanceSpecs` in `config.yaml`.

        They will be loaded *after* the extra modules specified in the **mod**
        parameter, and only in as far they have not been specifief in the
        **mod** parameter. In this way you can pass overriding
        checkout specifiers to the standard modules.

        See Also
        --------
        tf.advanced.settings: options allowed in `config.yaml`
        """

        app = self.app
        aContext = app.context
        moduleSpecs = aContext.moduleSpecs
        seen = self.seen

        for m in moduleSpecs or []:
            org = m["org"]
            repo = m["repo"]
            relative = m["relative"]
            checkout = m.get("checkout", self.checkout)
            ref = f"{org}/{repo}/{relative}"
            if ref in seen:
                continue

            if not self.getModule(
                org,
                repo,
                relative,
                checkout,
                specs=m,
            ):
                self.good = False

    def getRefs(self):
        """Get data from additional modules.

        These are specified in the `moduleRefs` parameter of `AppData`.
        We store the set of special modules in order to skip them
        later when we are loading the standard modules.
        """

        refs = self.moduleRefs
        for ref in refs:
            refPure = ref.rsplit(":", 1)[0]
            if refPure in self.seen:
                continue

            parts = splitModRef(ref)
            if not parts:
                self.good = False
                continue

            parts[2] = normpath(parts[2])  # the relative bit

            if not self.getModule(*parts):
                self.good = False

    def getModules(self):
        """Get data from additional local directories.

        These are specified in the `locations` and `modules` parameters of `AppData`.
        """

        self.provenance = []
        provenance = self.provenance
        self.mLocations = []
        mLocations = self.mLocations

        self.locations = None
        self.modules = None

        self.good = True
        self.seen = set()

        self.getMain()
        self.getRefs()
        self.getStandard()

        version = self.version
        good = self.good
        app = self.app

        if good:
            app.mLocations = mLocations
            app.provenance = provenance
        else:
            return

        mModules = []
        if mLocations:
            mModules.append(version or "")

        locations = self.locationsArg
        modules = self.modulesArg

        givenLocations = (
            []
            if locations is None
            else [expandDir(app, x.strip()) for x in itemize(locations, "\n")]
            if type(locations) is str
            else [str(x) for x in locations]
        )
        givenModules = (
            []
            if modules is None
            else [normpath(x.strip()) for x in itemize(modules, "\n")]
            if type(modules) is str
            else [normpath(str(x)) for x in modules]
        )

        self.locations = mLocations + givenLocations
        self.modules = mModules + givenModules

    def getModule(self, org, repo, relative, checkout, isBase=False, specs=None):
        """Prepare to load a single module.

        Eventually, all TF data will be downloaded from local directories, bases
        on a list of location paths and module paths.

        This function computes the contribution of a single module to both the
        location paths and the module paths.

        Parameters
        ----------
        org: string
            GitHub organization of the module
        repo: string:
            GitHub repository of the module
        relative: string
            Path within the repository of the module
        checkout: string
            A specifier to use a specific release or commit of a data repository.
        isBase: boolean, optional `False`
            Whether this module is the main data of the corpus.
        specs: dict, optional `False`
            Additional informational attributes of the module, e.g. a DOI
        """

        host = self.host
        version = self.version
        silent = self.silent
        mLocations = self.mLocations
        provenance = self.provenance
        seen = self.seen
        app = self.app
        _browse = app._browse
        aContext = app.context

        relative = normpath(relative)

        moduleRef = f"{org}/{repo}/{relative}"
        if moduleRef in self.seen:
            return True

        if org is None or repo is None:
            repoLocation = relative
            mLocations.append(relative)
            (commit, local, release) = (None, None, None)
        else:
            (commit, release, local, localBase, localDir) = checkoutRepo(
                _browse=_browse,
                host=host,
                org=org,
                repo=repo,
                folder=relative,
                version=version,
                checkout=checkout,
                withPaths=False,
                keep=False,
                silent=silent,
            )
            if not localBase:
                return False

            repoLocation = f"{localBase}/{org}/{repo}"
            mLocations.append(f"{localBase}/{localDir}")

        seen.add(moduleRef)
        if isBase:
            app.repoLocation = repoLocation

        info = {}
        for item in (
            ("doi", None),
            ("corpus", f"{org}/{repo}/{relative}"),
        ):
            (key, default) = item
            info[key] = (
                getattr(aContext, key)
                if isBase
                else specs[key]
                if specs and key in specs
                else default
            )
        provenance.append(
            (
                ("corpus", info["corpus"]),
                ("version", version),
                ("commit", commit or "??"),
                ("release", release or "none"),
                (
                    "live",
                    provenanceLink(
                        host, org, repo, version, commit, local, release, relative
                    ),
                ),
                ("doi", info["doi"]),
            )
        )
        return True


def getModulesData(*args):
    """Retrieve all data for a corpus.

    Parameters
    ----------
    args: list
        All parameters needed to retrieve all associated data.
        They are the same as are needed to construct an `AppData` object.
    """

    mData = AppData(*args)
    mData.getModules()
    if mData.locations is None:
        return None
    return (mData.locations, mData.modules)
