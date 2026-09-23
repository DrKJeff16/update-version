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

from typing import Any


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

    def __init__(self, all_versions: list[tuple[int, int, int]]):
        """
        Initialize VersionInfo object.

        Parameters
        ----------
        all_versions : list[tuple[int, int, int]]
            A list of tuples of three-integers, containing (in order) the major, minor and patch
            components.
        """
        all_versions.sort()

        self.all_versions = all_versions.copy()
        self.major = self.all_versions[::-1][0][0]
        self.minor = self.all_versions[::-1][0][1]
        self.patch = self.all_versions[::-1][0][2]

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
        return self.major, self.minor, self.patch

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
            suffix = " (latest)" if i == len(self.all_versions) - 1 else "\n"
            result += f"{info[0]}.{info[1]}.{info[2]}{suffix}"

        return result


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

    def __init__(self, *opts: list[str], **kwargs):
        self.opts = [opt for opt in opts]
        self.kwargs = kwargs


# vim: set ts=4 sts=4 sw=4 et ai si sta:
