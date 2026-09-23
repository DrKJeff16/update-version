from typing import Any

__all__ = ['ParserSpec', 'VersionInfo']

class VersionInfo:
    """
    A ``sys.version_info``-like object type.

    Parameters
    ----------
    all_versions : list[tuple[int, int, int]]
        A list of three number tuples, containing (in order) the major, minor and patch
        components.

    Attributes
    ----------
    major : int
        The major component of the version.
    minor : int
        The minor component of the version.
    patch : int
        The patch component of the version.
    all_versions : list[tuple[int, int, int]]
        A list of tuples containing all the versions in the object instance.

    Methods
    -------
    get_all_versions()

    See Also
    --------
    sys.version_info
        The object instance this is based from.
    """
    all_versions: list[tuple[int, int, int]]
    major: int
    minor: int
    patch: int
    def __init__(self, all_versions: list[tuple[int, int, int]]) -> None:
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : list[tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
    def __eq__(self, b) -> bool:
        """
        Check the equality between two ``VersionInfo`` instances.

        Parameters
        ----------
        b : VersionInfo
            The other instance to compare.

        Returns
        -------
        bool
            Whether they are equal or not.
        """
    def get_current_version(self) -> tuple[int, int, int]:
        """
        Get a tuple representing the current version.

        Returns
        -------
        major : int
            Major component.
        minor : int
            Minor component.
        patch : int
            Patch component.
        """
    def get_all_versions(self) -> str:
        """
        Retrieve all versions as a string.

        Returns
        -------
        str
            A string, containing the program versions, in ascending order.

        Examples
        --------
        To generate a single string.
        >>> from update_version.version import VersionInfo
        >>> print(VersionInfo([(0, 0, 1), (0, 0, 2), (0, 1, 0)]).get_all_versions())
        0.0.1
        0.0.2
        0.0.3 (latest)
        """

class ParserSpec:
    """
    Stores the spec for ``argparse`` operations in a constant value.

    Parameters
    ----------
    *opts
        A list containing all the relevant iterations of the same option.
    **kwargs
        Extra arguments for ``argparse.ArgumentParser``.

    Attributes
    ----------
    opts : list[str]
        A list containing all the relevant iterations of the same option.
    kwargs : dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    """
    opts: list[str]
    kwargs: dict[str, Any]
    def __init__(self, *opts: list[str], **kwargs) -> None: ...
