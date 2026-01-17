from _typeshed import Incomplete

from .types import VersionInfo as VersionInfo

__all__ = ['VersionInfo', 'list_versions', 'version_info', 'version_print', '__version__']

version_info: Incomplete
__version__: str

def list_versions() -> None:
    """List all versions."""
def version_print(version: str) -> None:
    """
    Print project version, then exit.

    Parameters
    ----------
    version : str
        The version string.
    """

# vim: set ts=4 sts=4 sw=4 et ai si sta:
