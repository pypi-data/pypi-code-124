import os
import sys
from pathlib import Path
from textwrap import dedent

# __all__ is also corrected below.
__all__ = list("Qt" + body for body in
    "Core;Gui;Widgets;PrintSupport;Sql;Network;Test;Concurrent;Designer;Xml;Help;Multimedia;MultimediaWidgets;OpenGL;OpenGLWidgets;Positioning;NetworkAuth;Nfc;Qml;Quick;Quick3D;QuickControls2;QuickWidgets;RemoteObjects;Scxml;Sensors;SerialPort;StateMachine;Charts;Svg;SvgWidgets;DataVisualization;Bluetooth;UiTools;WebChannel;WebEngineCore;WebEngineWidgets;WebEngineQuick;WebSockets;DBus;3DCore;3DRender;3DInput;3DLogic;3DAnimation;3DExtras"
    .split(";"))
__version__ = "6.3.1"
__version_info__ = (6, 3, 1, "", "")


def _additional_dll_directories(package_dir):
    # Find shiboken6 relative to the package directory.
    root = Path(package_dir).parent
    # Check for a flat .zip as deployed by cx_free(PYSIDE-1257)
    if root.suffix == '.zip':
        return []
    shiboken6 = root / 'shiboken6'
    if shiboken6.is_dir(): # Standard case, only shiboken6 is needed
        return [shiboken6]
    # The below code is for the build process when generate_pyi.py
    # is executed in the build directory. We need libpyside and Qt in addition.
    shiboken6 = Path(root).parent / 'shiboken6' / 'libshiboken'
    if not shiboken6.is_dir():
        raise ImportError(str(shiboken6) + ' does not exist')
    result = [shiboken6, root / 'libpyside']
    libpysideqml = root / 'libpysideqml'
    if libpysideqml.is_dir():
        result.append(libpysideqml)
    for path in os.environ.get('PATH').split(';'):
        if path:
             if (Path(path) / 'qmake.exe').exists():
                 result.append(path)
                 break
    return result


def _setupQtDirectories():
    # On Windows we need to explicitly import the shiboken6 module so
    # that the libshiboken.dll dependency is loaded by the time a
    # Qt module is imported. Otherwise due to PATH not containing
    # the shiboken6 module path, the Qt module import would fail
    # due to the missing libshiboken dll.
    # In addition, as of Python 3.8, the shiboken package directory
    # must be added to the DLL search paths so that shiboken6.dll
    # is found.
    # We need to do the same on Linux and macOS, because we do not
    # embed rpaths into the PySide6 libraries that would point to
    # the libshiboken library location. Importing the module
    # loads the libraries into the process memory beforehand, and
    # thus takes care of it for us.

    pyside_package_dir = Path(__file__).parent.resolve()

    if sys.platform == 'win32' and sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        for dir in _additional_dll_directories(pyside_package_dir):
            os.add_dll_directory(os.fspath(dir))

    try:
        # PYSIDE-1497: we use the build dir or install dir or site-packages, whatever the path
        #              setting dictates. There is no longer a difference in path structure.
        from shiboken6 import Shiboken
    except Exception:
        paths = ', '.join(sys.path)
        print(f"PySide6/__init__.py: Unable to import Shiboken from {paths}",
              file=sys.stderr)
        raise

    #   Trigger signature initialization.
    try:
        # PYSIDE-829: Avoid non-existent attributes in compiled code (Nuitka).
        # We now use an explicit function instead of touching a signature.
        _init_pyside_extension()
    except (AttributeError, NameError):
        stars = 79 * "*"
        fname = Shiboken.__file__
        print(dedent(f'''\
            {stars}
            PySide6/__init__.py: The `signature` module was not initialized.
            This libshiboken module was loaded from

            "{fname}".

            Please make sure that this is the real Shiboken binary and not just a folder.
            {stars}
            '''), file=sys.stderr)
        raise

    if sys.platform == 'win32':
        # PATH has to contain the package directory, otherwise plugins
        # won't be able to find their required Qt libraries (e.g. the
        # svg image plugin won't find Qt5Svg.dll).
        os.environ['PATH'] = os.fspath(pyside_package_dir) + os.pathsep + os.environ['PATH']

        # On Windows, add the PySide6\openssl folder (created by setup.py's
        # --openssl option) to the PATH so that the SSL DLLs can be found
        # when Qt tries to dynamically load them. Tell Qt to load them and
        # then reset the PATH.
        openssl_dir = pyside_package_dir / 'openssl'
        if openssl_dir.exists():
            path = os.environ['PATH']
            try:
                os.environ['PATH'] = os.fspath(openssl_dir) + os.pathsep + path
                try:
                    from . import QtNetwork
                except ImportError:
                    pass
                else:
                    QtNetwork.QSslSocket.supportsSsl()
            finally:
                os.environ['PATH'] = path


def _find_all_qt_modules():
    # Since the wheel split, the __all__ variable cannot be computed statically,
    # because we don't know all modules in advance.

    # Instead, we look into the file system and quickly build a list of all
    # existing .pyi files, because importing is not desired and also impossible during import.
    # By using the initially created list, we can keep some order intact.
    location = Path(__file__).resolve().parent

    # Note: We should _not_ call this function while still building, but use the existing value!
    in_build = Path("/home/qt/work/pyside/pyside-setup/build/qfpa-py3.8-qt6.3.1-64bit-release/build/pyside6") in location.parents

    if in_build:
        return __all__

    files = os.listdir(location)
    unordered = set(name[:-4] for name in files if name.startswith("Qt") and name.endswith(".pyi"))
    ordered_part = __all__
    result = []
    for name in ordered_part:
        if name in unordered:
            result.append(name)
            unordered.remove(name)
    result.extend(unordered)
    return result


__all__ = _find_all_qt_modules()
_setupQtDirectories()
