# PYTHON_ARGCOMPLETE_OK
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Version updater from a target file.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
from os.path import isfile, realpath
from re import match
from typing import List

from .args.parsing import arg_parser_init
from .util import die, verbose_print
from .version import __version__, list_versions, version_print

PATH: str = realpath("./version.txt")


def convert_to_version(
    data: str,
    dashed: bool
) -> List[int]:
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


def retrieve_version(
    path: str,
    dashed: bool
) -> List[int]:
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
    with open(PATH, "r") as file:
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

    minor: bool = ns.minor
    major: bool = ns.major
    patch: bool = ns.patch
    extra: bool = ns.extra
    dry_run: bool = ns.dry_run
    dashed: bool = ns.dashed
    verbose: bool = ns.verbose
    print_version: bool = ns.print_version

    if dry_run:
        verbose = True

    if extra:
        dashed = True

    if not (minor or major or patch or extra):
        patch = True

    replace: List[int] = convert_to_version(
        "".join(ns.replace) if ns.replace is not str else ns.replace,
        dashed
    )
    old_version: List[int] = retrieve_version(path, dashed)
    old_str: str = gen_version_str(old_version, dashed)

    if print_version:
        version_print(old_str, "")

    new_version: List[str] = list()
    if len(replace) == 0:
        new_version = [str(n + 1 if cond else n)
                       for n, cond in zip(old_version, (major, minor, patch, extra))]
    else:
        new_version = [str(x) for x in replace]

    new_str: str = gen_version_str(new_version, dashed)
    verbose_print(f"{old_str}  ==>  {new_str}", verbose=verbose)
    if dry_run:
        return 0

    with open(path, "w") as file:
        file.write(new_str + "\n")

    return 0

# vim: set ts=4 sts=4 sw=4 et ai si sta:
