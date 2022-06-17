import ctypes as ct
import platform
import winreg
from pathlib import Path

from .error import InstallError

bits = 64 if ct.sizeof(ct.c_voidp) == 8 else 32

if platform.system() != "Windows":
    raise InstallError("Only Windows OS supported")


VM_KEY = "VB:Voicemeeter {17359A74-1236-5467}"
REG_KEY = "".join(
    [
        "SOFTWARE",
        ("\\WOW6432Node" if bits == 64 else ""),
        "\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
    ]
)


def get_vmpath():
    with winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, r"{}".format(REG_KEY + "\\" + VM_KEY)
    ) as vm_key:
        path = winreg.QueryValueEx(vm_key, r"UninstallString")[0]
    return path


vm_path = Path(get_vmpath())
vm_parent = vm_path.parent

DLL_NAME = f'VoicemeeterRemote{"64" if bits == 64 else ""}.dll'

dll_path = vm_parent.joinpath(DLL_NAME)
if not dll_path.is_file():
    raise InstallError(f"Could not find {DLL_NAME}")

libc = ct.CDLL(str(dll_path))
