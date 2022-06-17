from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

from matplotlib.figure import Axes

from pygenomeviz.feature import Feature
from pygenomeviz.genbank import Genbank
from pygenomeviz.link import Link


class Track:
    """Track BaseClass"""

    def __init__(
        self,
        name: str,
        size: int,
        labelsize: int = 0,
        spines: bool = False,
        ratio: float = 1.0,
    ):
        """
        Parameters
        ----------
        name : str
            Track name
        size : int
            Track size
        labelsize : int, optional
            Track label size
        spines : bool, optional
            Display track spines
        ratio : float, optional
            Track height ratio
        """
        self.name = name
        self.size = size
        self.labelsize = labelsize
        self.spines = spines
        self.ratio = ratio
        self._offset: Optional[int] = None
        self._ax: Optional[Axes] = None

    @property
    def zorder(self) -> float:
        """Track zorder"""
        return 0

    @property
    def ylim(self) -> Tuple[float, float]:
        """Track y min-max limit tuple"""
        return (-1.0, 1.0)

    @property
    def tick_params(self) -> Dict[str, bool]:
        """Track tick parameters dict"""
        return {
            "left": False,
            "labelleft": False,
            "bottom": False,
            "labelbottom": False,
        }

    @property
    def spines_params(self) -> Dict[str, bool]:
        """Spines parameters dict"""
        return {
            "left": self.spines,
            "right": self.spines,
            "top": self.spines,
            "bottom": self.spines,
        }

    @property
    def offset(self) -> int:
        """Track alignment offset"""
        if self._offset is None:
            err_msg = "Can't access offset property before calling 'plotfig' method."
            raise ValueError(err_msg)
        return self._offset

    @property
    def ax(self) -> Axes:
        """Track axes

        Can't access ax property before calling GenomeViz class `plotfig` method.

        Returns
        -------
        ax : Axes
            Track matplotlib axes object
            - xlim = `(0, gv.max_track_size)`
            - ylim = `(-1, 1)`
        """
        if self._ax is None:
            err_msg = "Can't access ax property before calling 'plotfig' method."
            raise ValueError(err_msg)
        return self._ax


class FeatureTrack(Track):
    """FeatureTrack Class"""

    def __init__(
        self,
        name: str,
        size: int,
        labelsize: int = 20,
        labelmargin: float = 0.01,
        linewidth: int = 1,
        linecolor: str = "black",
        spines: bool = False,
        ratio: float = 1.0,
    ):
        """
        Parameters
        ----------
        name : str
            Track name
        size : int
            Track size
        labelsize : int, optional
            Track label size
        labelmargin : float, optional
            Track label margin
        linewidth : int, optional
            Track line width
        linecolor : str, optional
            Track line color
        spines : bool, optional
            Display track spines
        ratio : float, optional
            Track height ratio
        """
        super().__init__(name, size, labelsize, spines, ratio)
        self.labelmargin = labelmargin
        self.linewidth = linewidth
        self.linecolor = linecolor
        self.features: List[Feature] = []
        self.subtracks: List[FeatureSubTrack] = []

    @property
    def zorder(self) -> float:
        """Track zorder"""
        return 10

    @property
    def label_params(self) -> Dict[str, Any]:
        """Label drawing parameters"""
        return {
            "s": self.name,
            "fontsize": self.labelsize,
            "ha": "right",
            "va": "center",
        }

    def add_feature(
        self,
        start: int,
        end: int,
        strand: int,
        label: str = "",
        labelsize: int = 15,
        labelcolor: str = "black",
        plotstyle: str = "bigarrow",
        facecolor: str = "orange",
        edgecolor: str = "black",
        linewidth: float = 0,
        labelrotation: int = 45,
        labelvpos: str = "strand",
        labelhpos: str = "center",
        labelha: str = "left",
        arrow_shaft_ratio: float = 0.5,
        size_ratio: float = 0.9,
    ) -> None:
        """Add feature to track

        Parameters
        ----------
        start : int
            Featrue start position
        end : int
            Feature end position
        strand : int
            Feature strand
        label : str, optional
            Feature label
        labelsize : int, optional
            Feature label size
        labelcolor : str, optional
            Feature label color
        plotstyle : str, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`)
        facecolor : str, optional
            Feature facecolor
        edgecolor : str, optional
            Feature edgecolor
        linewidth : float, optional
            Feature edge linewidth
        labelrotation : int, optional
            Feature label rotation
        labelvpos : str, optional
            Feature label vertical position (`top`|`center`|`bottom`|`strand`)
            If 'strand' is set, 'top' or 'bottom' is auto selected by strand.
        labelhpos : str, optional
            Feature label horizontal position (`left`|`center`|`right`)
        labelha : str, optional
            Feature label horizontal alignment (`left`|`center`|`right`)
        arrow_shaft_ratio : float, optional
            Feature arrow shaft ratio
        size_ratio : float, optional
            Feature size ratio to track
        """
        self.features.append(
            Feature(
                start,
                end,
                strand,
                label,
                labelsize,
                labelcolor,
                plotstyle,
                facecolor,
                edgecolor,
                linewidth,
                labelrotation,
                labelvpos,
                labelhpos,
                labelha,
                arrow_shaft_ratio,
                size_ratio,
            )
        )

    def add_genbank_features(
        self,
        gbk: Genbank,
        feature_type: str = "CDS",
        label_type: Optional[str] = None,
        label_filter: Optional[List[str]] = None,
        allow_partial: bool = True,
        labelsize: int = 15,
        labelcolor: str = "black",
        plotstyle: str = "bigarrow",
        facecolor: str = "orange",
        edgecolor: str = "black",
        linewidth: float = 0,
        labelrotation: int = 45,
        labelvpos: str = "strand",
        labelhpos: str = "center",
        labelha: str = "left",
        arrow_shaft_ratio: float = 0.5,
        size_ratio: float = 0.9,
    ):
        """Add features from genbank record

        Parameters
        ----------
        gbk : Genbank
            Genbank object
        feature_type : str, optional
            Feature type (e.g. `CDS`,`rRNA`,`tRNA`,etc...)
        label_type : Optional[str], optional
            Label type (e.g. `gene`,`protein_id`,`product`,etc...)
        label_filter : Optional[List[str]], optional
            Label filter string list (e.g. `hypothetical`, `uncharacterized`)
            If label contains target string, make it empty.
        allow_partial : bool, optional
            If True, features that are partially included in range are also extracted
        labelsize : int, optional
            Feature label size
        labelcolor : str, optional
            Feature label color
        plotstyle : str, optional
            Feature plot style (`bigarrow`|`arrow`|`bigbox`|`box`)
        facecolor : str, optional
            Feature facecolor
        edgecolor : str, optional
            Feature edgecolor
        linewidth : float, optional
            Feature edge linewidth
        labelrotation : int, optional
            Feature label rotation
        labelvpos : str, optional
            Feature label vertical position (`top`|`center`|`bottom`|`strand`)
        labelhpos : str, optional
            Feature label horizontal position (`left`|`center`|`right`)
        labelha : str, optional
            Feature label horizontal alignment (`left`|`center`|`right`)
        arrow_shaft_ratio : float, optional
            Feature arrow shaft ratio
        size_ratio : float, optional
            Feature size ratio to track
        """
        target_features = gbk.extract_features(feature_type, None, True, allow_partial)
        for feature in target_features:
            start = int(str(feature.location.start))
            end = int(str(feature.location.end))
            strand = feature.strand
            if label_type is None:
                label = ""
            else:
                label = feature.qualifiers.get(label_type, [""])[0]
                if label_filter is not None:
                    for filter_str in label_filter:
                        label = "" if filter_str in label else label
            self.features.append(
                Feature(
                    start,
                    end,
                    strand,
                    label,
                    labelsize,
                    labelcolor,
                    plotstyle,
                    facecolor,
                    edgecolor,
                    linewidth,
                    labelrotation,
                    labelvpos,
                    labelhpos,
                    labelha,
                    arrow_shaft_ratio,
                    size_ratio,
                )
            )


class FeatureSubTrack(Track):
    """FeatureSubTrack Class"""

    def __init__(self, name: str, size: int, spines: bool = False, ratio: float = 1.0):
        super().__init__(name, size, 0, spines, ratio)


class LinkTrack(Track):
    """LinkTrack Class"""

    def __init__(self, name: str, spines: bool = False, ratio: float = 1.0):
        """
        Parameters
        ----------
        name : str
            Track name
        spines : bool, optional
            Display track spines
        ratio : float, optional
            Track height ratio
        """
        super().__init__(name, 0, 0, spines, ratio)
        self.links: List[Link] = []

    def add_link(self, link: Link) -> None:
        """Add link to track

        Parameters
        ----------
        link : Link
            Link between feature track
        """
        self.links.append(link)


class TickTrack(Track):
    """TickTrack Class"""

    def __init__(
        self,
        size: int,
        labelsize: int = 15,
        spines: bool = False,
        ratio: float = 1.0,
        tick_style: str = "bar",
    ):
        """
        Parameters
        ----------
        size : int
            Track size
        labelsize : int, optional
            Tick label size
        spines : bool, optional
            Display track spines
        ratio : float, optional
            Track height ratio
        tick_style : str, optional
            Tick style (`axis`|`bar`)
        """
        super().__init__("tick", size, labelsize, spines, ratio)
        self.tick_style = tick_style

    @property
    def tick_params(self) -> Dict[str, Any]:
        """Track tick parameters dict"""
        return {
            "left": False,
            "labelleft": False,
            "bottom": self.tick_style == "axis",
            "labelbottom": self.tick_style == "axis",
            "labelsize": self.labelsize,
        }

    @property
    def spines_params(self) -> Dict[str, bool]:
        """Spines parameters dict"""
        return {
            "left": self.spines,
            "right": self.spines,
            "top": self.spines,
            "bottom": self.spines or self.tick_style == "axis",
        }

    @property
    def scalebar_text_params(self) -> Dict[str, Any]:
        """Scalebar text parameters dict"""
        return {
            "x": self.xcenter,
            "y": self.ymin,
            "s": self.scalebar_label,
            "fontsize": self.labelsize,
            "ha": "center",
            "va": "top",
        }

    @property
    def unit(self) -> str:
        """Unit (bp, Kb, Mb, Gb)"""
        for unit, value in self.unit2base_value.items():
            if self.size >= value:
                return unit
        raise ValueError("Unexpected error.")

    @property
    def format_str(self) -> str:
        """Format string ('.0f' or '.1f')"""
        if self.size / self.base_value >= 10:
            return ".0f"
        else:
            return ".1f"

    @property
    def base_value(self) -> float:
        """Base value"""
        return self.unit2base_value[self.unit]

    @property
    def unit2base_value(self) -> Dict[str, int]:
        """Unit & base value dict"""
        return {"Gb": 10**9, "Mb": 10**6, "Kb": 10**3, "bp": 1}

    @property
    def scalebar_label(self) -> str:
        """Label"""
        label = f"{self.scalebar_size / self.base_value:{self.format_str}}"
        return f"{label} {self.unit}"

    @property
    def xmin(self) -> float:
        """xmin"""
        return self.size - self.scalebar_size

    @property
    def xmax(self) -> float:
        """xmax"""
        return self.size

    @property
    def xcenter(self) -> float:
        """xcenter"""
        return (self.xmin + self.xmax) / 2

    @property
    def ymin(self) -> float:
        """ymin"""
        return self.ylim[0] - abs(self.ylim[0] * 0.1)

    @property
    def ycenter(self) -> float:
        """ycenter"""
        return self.ylim[0]

    @property
    def ymax(self) -> float:
        """ymax"""
        return self.ylim[0] + abs(self.ylim[0] * 0.1)

    @property
    def scalebar_size(self) -> float:
        """Scalebar size"""
        min_scalebar_size = self.size * 0.1
        unit = int(10 ** (len(str(int(min_scalebar_size))) - 1))
        value = math.ceil(min_scalebar_size / unit)
        steps = [1, 2, 5, 10]
        for i in range(0, len(steps) - 1):
            if steps[i] < value < steps[i + 1]:
                return steps[i + 1] * unit
        return value * unit

    def tick_formatter(self, value: float, pos: int) -> str:
        """Tick formatter

        Parameters
        ----------
        value : float
            Format target tick value
        pos : int
            Tick position (Not used for value formatting)

        Returns
        -------
        format_value : str
            Format tick value string
        """
        tick_value = value / self.base_value
        return f"{tick_value:{self.format_str}} {self.unit}"
