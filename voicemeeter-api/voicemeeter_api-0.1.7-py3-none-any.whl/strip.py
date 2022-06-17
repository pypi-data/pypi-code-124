import time
from abc import abstractmethod
from math import log
from typing import Union

from .error import VMError
from .iremote import IRemote
from .kinds import kinds_all
from .meta import bool_prop


class Strip(IRemote):
    """
    Implements the common interface

    Defines concrete implementation for strip
    """

    @abstractmethod
    def __str__(self):
        pass

    @property
    def identifier(self) -> str:
        return f"strip[{self.index}]"

    @property
    def mono(self) -> bool:
        return self.getter("mono") == 1

    @mono.setter
    def mono(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("mono is a boolean parameter")
        self.setter("mono", 1 if val else 0)

    @property
    def solo(self) -> bool:
        return self.getter("solo") == 1

    @solo.setter
    def solo(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("solo is a boolean parameter")
        self.setter("solo", 1 if val else 0)

    @property
    def mute(self) -> bool:
        return self.getter("mute") == 1

    @mute.setter
    def mute(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("mute is a boolean parameter")
        self.setter("mute", 1 if val else 0)

    @property
    def limit(self) -> int:
        return int(self.getter("limit"))

    @limit.setter
    def limit(self, val: int):
        self.setter("limit", val)

    @property
    def label(self) -> str:
        return self.getter("Label", is_string=True)

    @label.setter
    def label(self, val: str):
        if not isinstance(val, str):
            raise VMError("label is a string parameter")
        self.setter("Label", val)

    @property
    def gain(self) -> float:
        return round(self.getter("gain"), 1)

    @gain.setter
    def gain(self, val: float):
        self.setter("gain", val)

    def fadeto(self, target: float, time_: int):
        self.setter("FadeTo", f"({target}, {time_})")
        time.sleep(self.remote.delay)

    def fadeby(self, change: float, time_: int):
        self.setter("FadeBy", f"({change}, {time_})")
        time.sleep(self.remote.delay)


class PhysicalStrip(Strip):
    def __str__(self):
        return f"{type(self).__name__}{self.index}"

    @property
    def comp(self) -> float:
        return round(self.getter("Comp"), 1)

    @comp.setter
    def comp(self, val: float):
        self.setter("Comp", val)

    @property
    def gate(self) -> float:
        return round(self.getter("Gate"), 1)

    @gate.setter
    def gate(self, val: float):
        self.setter("Gate", val)

    @property
    def audibility(self) -> float:
        return round(self.getter("audibility"), 1)

    @audibility.setter
    def audibility(self, val: float):
        self.setter("audibility", val)

    @property
    def device(self):
        return self.getter("device.name", is_string=True)

    @property
    def sr(self):
        return int(self.getter("device.sr"))


class VirtualStrip(Strip):
    def __str__(self):
        return f"{type(self).__name__}{self.index}"

    @property
    def mc(self) -> bool:
        return self.getter("mc") == 1

    @mc.setter
    def mc(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("mc is a boolean parameter")
        self.setter("mc", 1 if val else 0)

    mono = mc

    @property
    def k(self) -> int:
        return int(self.getter("karaoke"))

    @k.setter
    def k(self, val: int):
        self.setter("karaoke", val)

    @property
    def bass(self):
        return round(self.getter("EQGain1"), 1)

    @bass.setter
    def bass(self, val: float):
        self.setter("EQGain1", val)

    @property
    def mid(self):
        return round(self.getter("EQGain2"), 1)

    @mid.setter
    def mid(self, val: float):
        self.setter("EQGain2", val)

    med = mid

    @property
    def treble(self):
        return round(self.getter("EQGain3"), 1)

    @treble.setter
    def treble(self, val: float):
        self.setter("EQGain3", val)

    def appgain(self, name: str, gain: float):
        self.setter("AppGain", f'("{name}", {gain})')

    def appmute(self, name: str, mute: bool = None):
        if not isinstance(mute, bool) and mute not in (0, 1):
            raise VMError("appmute is a boolean parameter")
        self.setter("AppMute", f'("{name}", {1 if mute else 0})')


class StripLevel(IRemote):
    def __init__(self, remote, index):
        super().__init__(remote, index)
        phys_map = tuple((i, i + 2) for i in range(0, remote.kind.phys_in * 2, 2))
        virt_map = tuple(
            (i, i + 8)
            for i in range(
                remote.kind.phys_in * 2,
                remote.kind.phys_in * 2 + remote.kind.virt_in * 8,
                8,
            )
        )
        self.level_map = phys_map + virt_map

    def getter(self, mode):
        """Returns a tuple of level values for the channel."""

        def fget(i):
            res = self._remote.get_level(mode, i)
            return round(20 * log(res, 10), 1) if res > 0 else -200.0

        range_ = self.level_map[self.index]
        return tuple(fget(i) for i in range(*range_))

    def getter_prefader(self):
        def fget(i):
            return round(20 * log(i, 10), 1) if i > 0 else -200.0

        range_ = self.level_map[self.index]
        return tuple(
            fget(i) for i in self._remote._strip_levels[range_[0] : range_[-1]]
        )

    @property
    def identifier(self) -> str:
        return f"Strip[{self.index}]"

    @property
    def prefader(self) -> tuple:
        return self.getter_prefader()

    @property
    def postfader(self) -> tuple:
        return self.getter(1)

    @property
    def postmute(self) -> tuple:
        return self.getter(2)

    @property
    def updated(self) -> tuple:
        return self._remote._strip_comp


class GainLayer(IRemote):
    def __init__(self, remote, index, i):
        super().__init__(remote, index)
        self._i = i

    @property
    def identifier(self) -> str:
        return f"Strip[{self.index}]"

    @property
    def gain(self):
        return self.getter(f"GainLayer[{self._i}]")

    @gain.setter
    def gain(self, val):
        self.setter(f"GainLayer[{self._i}]", val)


def _make_gainlayer_mixin(remote, index):
    """Creates a GainLayer mixin"""
    return type(
        f"GainlayerMixin",
        (),
        {
            "gainlayer": tuple(
                GainLayer(remote, index, i) for i in range(remote.kind.num_bus)
            )
        },
    )


def _make_channelout_mixin(kind):
    """Creates a channel out property mixin"""
    return type(
        f"ChannelOutMixin{kind}",
        (),
        {
            **{f"A{i}": bool_prop(f"A{i}") for i in range(1, kind.phys_out + 1)},
            **{f"B{i}": bool_prop(f"B{i}") for i in range(1, kind.virt_out + 1)},
        },
    )


__make_channelout_mixins = {
    kind.name: _make_channelout_mixin(kind) for kind in kinds_all
}


def strip_factory(is_phys_strip, remote, i) -> Union[PhysicalStrip, VirtualStrip]:
    """
    Factory method for strips

    Mixes in required classes

    Returns a physical or virtual strip subclass
    """
    STRIP_cls = PhysicalStrip if is_phys_strip else VirtualStrip
    CHANNELOUTMIXIN_cls = __make_channelout_mixins[remote.kind.name]

    _kls = (STRIP_cls, CHANNELOUTMIXIN_cls)
    if remote.kind.name == "potato":
        GAINLAYERMIXIN_cls = _make_gainlayer_mixin(remote, i)
        _kls += (GAINLAYERMIXIN_cls,)
    return type(
        f"{STRIP_cls.__name__}{remote.kind}",
        _kls,
        {
            "levels": StripLevel(remote, i),
        },
    )(remote, i)


def request_strip_obj(is_phys_strip, remote, i) -> Strip:
    """
    Strip entry point. Wraps factory method.

    Returns a reference to a strip subclass of a kind
    """
    return strip_factory(is_phys_strip, remote, i)
