# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Custom ``update_version`` objects.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "ParserSpec",
    "VersionInfo",
]

from typing import Any, Dict, List, Tuple, TypedDict

import argcomplete


class VersionInfo():
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
    all_versions: List[Tuple[int, int, int]]

    def __init__(self, all_versions: List[Tuple[int, int, int]]):
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : List[Tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
        self.all_versions = all_versions.copy()

        all_versions = all_versions.copy()[::-1]
        self.major = all_versions[0][0]
        self.minor = all_versions[0][1]
        self.patch = all_versions[0][2]

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
        return f"{self.major}.{self.minor}.{self.patch}"

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
        return self.__str__()

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
        if not isinstance(b, VersionInfo):
            return False

        return self.major == b.major and self.minor == b.minor and self.patch == b.patch

    def get_current_version(self) -> Tuple[int, int, int]:
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
        return (self.major, self. minor, self.patch)

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
        result = ""
        for i, info in enumerate(self.all_versions):
            result += f"{info[0]}.{info[1]}.{info[2]}"
            if i == len(self.all_versions) - 1:
                result += " (latest)"
            else:
                result += "\n"

        return result


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

    opts: List[str]
    kwargs: Dict[str, Any]
    completer: argcomplete.completers.FilesCompleter | None

# vim: set ts=4 sts=4 sw=4 et ai si sta:
