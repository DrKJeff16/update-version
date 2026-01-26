from typing import Any, TypedDict

import argcomplete

__all__ = ['ParserSpec', 'VersionInfo']

class VersionInfo:
    """
    A ``sys.version_info``-like object type.

    Parameters
    ----------
    all_versions : List[Tuple[int, int, int]]
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
    all_versions : List[Tuple[int, int, int]]
        A list of tuples containing all the versions in the object instance.

    Methods
    -------
    get_all_versions()

    See Also
    --------
    sys.version_info
        The object instance this is based from.
    """
    major: int
    minor: int
    patch: int
    all_versions: list[tuple[int, int, int]]
    def __init__(self, all_versions: list[tuple[int, int, int]]) -> None:
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : List[Tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
    def __str__(self) -> str:
        """
        Representate this object as a string.

        This is what is returned when using ``str(VersionInfo(...))``.

        Returns
        -------
        str
            The string representation of the instance.

        Examples
        --------
        Only one definition in constructor.

        >>> from update_version.version import VersionInfo
        >>> print(str(VersionInfo([(0, 0, 1)])))
        0.0.1

        Multiple definitions in constructor.

        >>> from update_version.version import VersionInfo
        >>> print(str(VersionInfo([(0, 0, 1), (0, 0, 2)])))
        0.0.2
        """
    def __repr__(self) -> str:
        """
        Representate this object as a string.

        This is what is returned when using ``print(VersionInfo(...))``.

        Returns
        -------
        str
            The string representation of the instance.

        Examples
        --------
        Only one definition in constructor.

        >>> from update_version.version import VersionInfo
        >>> print(repr(VersionInfo([(0, 0, 1)])))
        0.0.1

        Multiple definitions in constructor.

        >>> from update_version.version import VersionInfo
        >>> print(repr(VersionInfo([(0, 0, 1), (0, 0, 2)])))
        0.0.2
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

class ParserSpec(TypedDict):
    """
    Stores the spec for ``argparse`` operations in a constant value.

    This is a ``TypedDict``-like object.

    Attributes
    ----------
    opts : List[str]
        A list containing all the relevant iterations of the same option.
    kwargs : Dict[str, Any]
        Extra arguments for ``argparse.ArgumentParser``.
    completer: argcomplete.completers.FilesCompleter or None
        The ``argcomplete`` completer (or ``None``).
    """
    opts: list[str]
    kwargs: dict[str, Any]
    completer: argcomplete.completers.FilesCompleter | None

# vim: set ts=4 sts=4 sw=4 et ai si sta:
