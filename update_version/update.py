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
from .util import die

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


def main() -> int:
    """
    Execute the script.

    Returns
    -------
    int
        The exit code.
    """
    parser, ns = arg_parser_init()

    path: str = realpath("".join(ns.path) if ns.path is not str else ns.path)
    if not isfile(path):
        die(f"Unable to find `{path}`!", code=1)

    dashed: bool = ns.dashed
    minor: bool = ns.minor
    major: bool = ns.major
    patch: bool = ns.patch
    extra: bool = ns.extra

    patch = True if not (minor or major or patch or extra) else patch
    dashed = True if extra else dashed

    replace = convert_to_version(
        "".join(ns.replace) if ns.replace is not str else ns.replace,
        dashed
    )
    new_version_list: List[str] = list()
    if len(replace) == 0:
        old_version = retrieve_version(path, dashed)
        new_version_list = [str(n + 1 if cond else n)
                            for n, cond in zip(old_version, (major, minor, patch, extra))]
    else:
        new_version_list = [str(x) for x in replace]

    new_version = tuple(new_version_list)

    if dashed:
        new_str = ".".join(new_version[:-2]) + "." + "-".join(new_version[-2:]) + "\n"
    else:
        new_str = ".".join(new_version) + "\n"

    with open(path, "w") as file:
        file.write(new_str)

    return 0

# vim: set ts=4 sts=4 sw=4 et ai si sta:
