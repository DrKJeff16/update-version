# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Custom ``update_version`` versioning objects.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "VersionInfo",
    "__version__",
    "list_versions",
    "version_info",
    "version_print",
]

from .types import VersionInfo
from .util import die

version_info = VersionInfo([
    (0, 1, 0),
    (0, 1, 1),
    (0, 1, 2),
    (0, 1, 3),
    (0, 1, 4),
    (0, 1, 5),
])

__version__: str = str(version_info)


def list_versions() -> None:
    """List all versions."""
    die(version_info.get_all_versions(), code=0)


def version_print(version: str, prog: str = "update-version") -> None:
    """
    Print project version, then exit.

    Parameters
    ----------
    version : str
        The version string.
    prog : str, optional, default=``"update-version"``
        The program string (can be empty).
    """
    if prog != "":
        prog += " - "

    die(f"{prog}{version}", code=0)

# vim: set ts=4 sts=4 sw=4 et ai si sta:
