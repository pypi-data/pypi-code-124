"""Interface class implementation for the destination x path data.
"""

from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos


class PathDestXInterface(RevertInterface, AttrLinkingInterface):

    _dest_x: Int

    def _initialize_dest_x_if_not_initialized(self) -> None:
        """
        Initialize the _dest_x attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, '_dest_x'):
            return
        self._dest_x = Int(0)

        self._append_dest_x_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='PathDestXInterface')
    def _append_dest_x_linking_setting(self) -> None:
        """
        Append a dest_x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._dest_x, attr_name='dest_x')
        self._append_attr_to_linking_stack(
            attr=self._dest_x, attr_name='dest_x')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='PathDestXInterface')
    def dest_x(self) -> Int:
        """
        Get a x-coordinate of the destination point.

        Returns
        -------
        dest_x : Int
            X-coordinate of the destination point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
        ...     control_x=50, control_y=0,
        ...     dest_x=100, dest_y=50)
        >>> bezier_2d.dest_x = ap.Int(125)
        >>> bezier_2d.dest_x
        Int(125)
        """
        self._initialize_dest_x_if_not_initialized()
        return self._dest_x._copy()

    @dest_x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='PathDestXInterface')
    def dest_x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
        self._initialize_dest_x_if_not_initialized()
        self._dest_x.value = value

        self._append_dest_x_linking_setting()

    _dest_x_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_dest_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_dest_x_snapshots',
            value=int(self._dest_x._value), snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_dest_x_if_not_initialized()
        self._dest_x._value = self._dest_x_snapshots[snapshot_name]
