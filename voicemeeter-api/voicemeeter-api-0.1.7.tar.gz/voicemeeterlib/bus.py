import time
from abc import abstractmethod
from math import log
from typing import Union

from .error import VMError
from .iremote import IRemote
from .meta import bus_mode_prop


class Bus(IRemote):
    """
    Implements the common interface

    Defines concrete implementation for bus
    """

    @abstractmethod
    def __str__(self):
        pass

    @property
    def identifier(self) -> str:
        return f"bus[{self.index}]"

    @property
    def mute(self) -> bool:
        return self.getter("mute") == 1

    @mute.setter
    def mute(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("mute is a boolean parameter")
        self.setter("mute", 1 if val else 0)

    @property
    def mono(self) -> bool:
        return self.getter("mono") == 1

    @mono.setter
    def mono(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("mono is a boolean parameter")
        self.setter("mono", 1 if val else 0)

    @property
    def eq(self) -> bool:
        return self.getter("eq.On") == 1

    @eq.setter
    def eq(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("eq is a boolean parameter")
        self.setter("eq.On", 1 if val else 0)

    @property
    def eq_ab(self) -> bool:
        return self.getter("eq.ab") == 1

    @eq_ab.setter
    def eq_ab(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("eq_ab is a boolean parameter")
        self.setter("eq.ab", 1 if val else 0)

    @property
    def sel(self) -> bool:
        return self.getter("sel") == 1

    @sel.setter
    def sel(self, val: bool):
        if not isinstance(val, bool) and val not in (0, 1):
            raise VMError("sel is a boolean parameter")
        self.setter("sel", 1 if val else 0)

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
        time.sleep(self._remote.DELAY)

    def fadeby(self, change: float, time_: int):
        self.setter("FadeBy", f"({change}, {time_})")
        time.sleep(self._remote.DELAY)


class PhysicalBus(Bus):
    def __str__(self):
        return f"{type(self).__name__}{self.index}"

    @property
    def device(self) -> str:
        return self.getter("device.name", is_string=True)

    @property
    def sr(self) -> int:
        return int(self.getter("device.sr"))


class VirtualBus(Bus):
    def __str__(self):
        return f"{type(self).__name__}{self.index}"


class BusLevel(IRemote):
    def __init__(self, remote, index):
        super().__init__(remote, index)
        self.level_map = tuple(
            (i, i + 8)
            for i in range(0, (remote.kind.phys_out + remote.kind.virt_out) * 8, 8)
        )

    def getter(self):
        """Returns a tuple of level values for the channel."""

        def fget(i):
            return round(20 * log(i, 10), 1) if i > 0 else -200.0

        range_ = self.level_map[self.index]
        return tuple(fget(i) for i in self._remote._bus_levels[range_[0] : range_[-1]])

    @property
    def identifier(self) -> str:
        return f"Bus[{self.index}]"

    @property
    def all(self) -> tuple:
        return self.getter()

    @property
    def updated(self) -> tuple:
        return self._remote._bus_comp


def _make_bus_mode_mixin():
    """Creates a mixin of Bus Modes."""

    def identifier(self) -> str:
        return f"Bus[{self.index}].mode"

    return type(
        "BusModeMixin",
        (IRemote,),
        {
            "identifier": property(identifier),
            **{
                mode: bus_mode_prop(mode)
                for mode in [
                    "normal",
                    "amix",
                    "bmix",
                    "repeat",
                    "composite",
                    "tvmix",
                    "upmix21",
                    "upmix41",
                    "upmix61",
                    "centeronly",
                    "lfeonly",
                    "rearonly",
                ]
            },
        },
    )


def bus_factory(phys_bus, remote, i) -> Union[PhysicalBus, VirtualBus]:
    """
    Factory method for buses

    Returns a physical or virtual bus subclass
    """
    BUS_cls = PhysicalBus if phys_bus else VirtualBus
    BUSMODEMIXIN_cls = _make_bus_mode_mixin()
    return type(
        f"{BUS_cls.__name__}{remote.kind}",
        (BUS_cls,),
        {
            "levels": BusLevel(remote, i),
            "mode": BUSMODEMIXIN_cls(remote, i),
        },
    )(remote, i)


def request_bus_obj(phys_bus, remote, i) -> Bus:
    """
    Bus entry point. Wraps factory method.

    Returns a reference to a bus subclass of a kind
    """
    return bus_factory(phys_bus, remote, i)
