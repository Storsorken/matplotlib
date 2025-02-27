import matplotlib.cm as cm
from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.backend_bases import MouseButton
from matplotlib.collections import Collection, PathCollection
from matplotlib.colors import Colormap, Normalize
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text
from matplotlib.transforms import Transform
from matplotlib.ticker import Locator, Formatter

from numpy.typing import ArrayLike
import numpy as np
from collections.abc import Callable, Iterable, Sequence
from typing import Literal
from .typing import ColorType

class ClabelText(Text): ...

class ContourLabeler:
    labelFmt: str | Formatter | Callable[[float], str] | dict[float, str]
    labelManual: bool | Iterable[tuple[float, float]]
    rightside_up: bool
    labelLevelList: list[float]
    labelIndiceList: list[int]
    labelMappable: cm.ScalarMappable
    labelCValueList: list[ColorType]
    labelXYs: list[tuple[float, float]]
    def clabel(
        self,
        levels: ArrayLike | None = ...,
        *,
        fontsize: str | float | None = ...,
        inline: bool = ...,
        inline_spacing: float = ...,
        fmt: str | Formatter | Callable[[float], str] | dict[float, str] | None = ...,
        colors: ColorType | Sequence[ColorType] | None = ...,
        use_clabeltext: bool = ...,
        manual: bool | Iterable[tuple[float, float]] = ...,
        rightside_up: bool = ...,
        zorder: float | None = ...
    ) -> list[Text]: ...
    @property
    def labelFontProps(self) -> FontProperties: ...
    @property
    def labelFontSizeList(self) -> list[float]: ...
    @property
    def labelTextsList(self) -> list[Text]: ...
    def print_label(self, linecontour: ArrayLike, labelwidth: float) -> bool: ...
    def too_close(self, x: float, y: float, lw: float) -> bool: ...
    def set_label_props(self, label: Text, text: str, color: ColorType) -> None: ...
    def get_text(
        self,
        lev: float,
        fmt: str | Formatter | Callable[[float], str] | dict[float, str],
    ) -> str: ...
    def locate_label(
        self, linecontour: ArrayLike, labelwidth: float
    ) -> tuple[float, float, float]: ...
    def calc_label_rot_and_inline(
        self,
        slc: ArrayLike,
        ind: int,
        lw: float,
        lc: ArrayLike | None = ...,
        spacing: int = ...,
    ) -> tuple[float, list[ArrayLike]]: ...
    def add_label(
        self, x: float, y: float, rotation: float, lev: float, cvalue: ColorType
    ) -> None: ...
    def add_label_clabeltext(
        self, x: float, y: float, rotation: float, lev: float, cvalue: ColorType
    ) -> None: ...
    def add_label_near(
        self,
        x: float,
        y: float,
        inline: bool = ...,
        inline_spacing: int = ...,
        transform: Transform | Literal[False] | None = ...,
    ) -> None: ...
    def pop_label(self, index: int = ...) -> None: ...
    def labels(self, inline: bool, inline_spacing: int) -> None: ...
    def remove(self) -> None: ...

class ContourSet(cm.ScalarMappable, ContourLabeler):
    axes: Axes
    levels: Iterable[float]
    filled: bool
    linewidths: float | ArrayLike | None
    linestyles: None | Literal["solid", "dashed", "dashdot", "dotted"] | Iterable[
        Literal["solid", "dashed", "dashdot", "dotted"]
    ]
    hatches: Iterable[str | None]
    alpha: float | None
    origin: Literal["upper", "lower", "image"] | None
    extent: tuple[float, float, float, float] | None
    colors: ColorType | Sequence[ColorType]
    extend: Literal["neither", "both", "min", "max"]
    antialiased: bool | None
    nchunk: int
    locator: Locator | None
    logscale: bool
    negative_linestyles: None | Literal[
        "solid", "dashed", "dashdot", "dotted"
    ] | Iterable[Literal["solid", "dashed", "dashdot", "dotted"]]
    collections: list[PathCollection]
    labelTexts: list[Text]
    labelCValues: list[ColorType]
    allkinds: list[np.ndarray]
    tcolors: list[tuple[float, float, float, float]]

    # only for not filled
    tlinewidths: list[tuple[float]]

    def __init__(
        self,
        ax: Axes,
        *args,
        levels: Iterable[float] | None = ...,
        filled: bool = ...,
        linewidths: float | ArrayLike | None = ...,
        linestyles: Literal["solid", "dashed", "dashdot", "dotted"]
        | Iterable[Literal["solid", "dashed", "dashdot", "dotted"]]
        | None = ...,
        hatches: Iterable[str | None] = ...,
        alpha: float | None = ...,
        origin: Literal["upper", "lower", "image"] | None = ...,
        extent: tuple[float, float, float, float] | None = ...,
        cmap: str | Colormap | None = ...,
        colors: ColorType | Sequence[ColorType] | None = ...,
        norm: str | Normalize | None = ...,
        vmin: float | None = ...,
        vmax: float | None = ...,
        extend: Literal["neither", "both", "min", "max"] = ...,
        antialiased: bool | None = ...,
        nchunk: int = ...,
        locator: Locator | None = ...,
        transform: Transform | None = ...,
        negative_linestyles: Literal["solid", "dashed", "dashdot", "dotted"]
        | Iterable[Literal["solid", "dashed", "dashdot", "dotted"]]
        | None = ...,
        **kwargs
    ) -> None: ...
    def get_transform(self) -> Transform: ...
    def legend_elements(
        self, variable_name: str = ..., str_format: Callable[[float], str] = ...
    ) -> tuple[list[Artist], list[str]]: ...
    def get_alpha(self) -> float | None: ...
    def set_alpha(self, alpha: float | None) -> None: ...
    def find_nearest_contour(
        self, x: float, y: float, indices: Iterable[int] | None = ..., pixel: bool = ...
    ) -> tuple[Collection, int, int, float, float, float]: ...

class QuadContourSet(ContourSet): ...
