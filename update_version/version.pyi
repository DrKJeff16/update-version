from _typeshed import Incomplete

from .types import VersionInfo as VersionInfo

__all__ = ['VersionInfo', '__version__', 'list_versions', 'version_info', 'version_print']

version_info: Incomplete
__version__: str

def list_versions() -> None:
    """List all versions."""
def version_print(version: str, prog: str = 'update-version') -> None:
    '''
    Print project version, then exit.

    Parameters
    ----------
    version : str
        The version string.
    prog : str, optional, default=``"update-version"``
        The program string (can be empty).
    '''

# vim: set ts=4 sts=4 sw=4 et ai si sta:
