# PYTHON_ARGCOMPLETE_OK
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Core component for ``update_version``.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "convert_to_version",
    "gen_new_version",
    "gen_version_str",
    "main",
    "retrieve_version",
]

from io import TextIOWrapper
from os.path import isfile, realpath
from re import match
from typing import List, Tuple

from .args.parsing import arg_parser_init
from .util import die, verbose_print
from .version import __version__, list_versions, version_print


def convert_to_version(data: str, dashed: bool) -> List[int]:
    """
    Convert input string to version tuple.

    Parameters
    ----------
    data : str
        The input data.
    dashed : bool
        Whether the versioning spec uses dashes.

    Returns
    -------
    List[int]
        Major, Minor, Patch and (optionally) Dashed components (or an empty one if regex fails).
    """
    if data == "":
        return []

    match_str = "^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)"
    if dashed:
        match_str += "-[1-9][0-9]*"

    if match(match_str + "$", data) is None:
        die(f"Bad regex for `{data}`!", code=1)

    data_list = data.split(".")
    if dashed:
        last = data_list[2].split("-")
        if len(last) != 2:
            die("Badly formatted version string!", code=1)

        data_list[2] = last[0]
        data_list.append(last[1])

    return [int(x) for x in data_list]


def retrieve_version(path: str, dashed: bool) -> List[int]:
    """
    Get the version tuple from the version file.

    Parameters
    ----------
    path : str, optional
        The target file path.
    dashed : bool
        Whether the version is dashed or not.

    Returns
    -------
    List[int]
        Major, Minor and Patch components tuple.
    """
    with open(path, "r") as file:
        data: str = file.read().strip("\n")

    res = convert_to_version(data, dashed)
    if len(res) == 0:
        die("Bad conversion!", code=1)

    return res


def gen_version_str(version: List[int] | List[str], dashed: bool) -> str:
    """
    Generate the old version string.

    Parameters
    ----------
    version : List[int] or List[str]
        The version components separated (optionally as integers).
    dashed : bool
        Whether the versioning is dashed.

    Returns
    -------
    str
        The old version as a whole string.
    """
    data: List[str] = list()
    for ver in version:
        data.append(str(ver))

    if dashed:
        return ".".join(data[:-2]) + "." + "-".join(data[-2:])

    return ".".join(data)


def gen_new_version(
    old_version: List[int],
    replace: List[int],
    components: Tuple[bool, bool, bool, bool]
) -> List[str]:
    """
    Generate new version list.

    Parameters
    ----------
    old_version : List[int]
        The old version parsed as a list of integers.
    replace : List[int]
        The replaced version as a list of integers.
    components : Tuple[bool, bool, bool, bool]
        A tuple of booleans signaling, in order, the major, minor, patch and extra components.

    Returns
    -------
    List[str]
        A list of strings, each element is a version component, in order.
    """
    new_version: List[str] = list()

    if len(replace) == 0:
        new_version = [str(n + 1 if cond else n) for n, cond in zip(old_version, components)]
    else:
        new_version = [str(x) for x in replace]

    return new_version


def main() -> int:
    """
    Execute the script.

    Returns
    -------
    int
        The exit code.
    """
    parser, ns = arg_parser_init()

    if ns.version:
        version_print(__version__)

    if ns.list_versions:
        list_versions()

    path: str = realpath("".join(ns.path) if ns.path is not str else ns.path)
    if not isfile(path):
        die(f"Unable to find `{path}`!", code=1)

    dry_run: bool = ns.dry_run
    verbose: bool = True if dry_run else ns.verbose
    minor: bool = ns.minor
    major: bool = ns.major
    extra: bool = ns.extra
    patch: bool = True if not (minor or major or ns.patch or extra) else ns.patch
    dashed: bool = True if extra else ns.dashed
    print_version: bool = ns.print_version

    replace: List[int] = convert_to_version(
        "".join(ns.replace) if ns.replace is not str else ns.replace,
        dashed
    )
    old_version: List[int] = retrieve_version(path, dashed)
    old_str: str = gen_version_str(old_version, dashed)

    if print_version:
        version_print(old_str, "")

    new_str: str = gen_version_str(
        gen_new_version(old_version, replace, (major, minor, patch, extra)),
        dashed
    )
    verbose_print(f"{old_str}  ==>  {new_str}", verbose=verbose)

    if not dry_run:
        new_str += "\n" if new_str[-1] != "\n" else ""

        file: TextIOWrapper = open(path, "w")
        file.write(new_str)
        file.close()

    return 0

# vim: set ts=4 sts=4 sw=4 et ai si sta:
