# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Argument parsing utilities for ``update-version``.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "bootstrap_args",
    "arg_parser_init",
]

from argparse import ArgumentDefaultsHelpFormatter, ArgumentError, ArgumentParser, Namespace
from typing import List, Tuple

from ..types import ParserSpec
from ..util import die


def bootstrap_args(parser: ArgumentParser, specs: List[ParserSpec]) -> Namespace:
    """
    Bootstrap the program arguments.

    Parameters
    ----------
    parser : argparse.ArgumentParser
        The ``argparse.ArgumentParser`` object.
    specs : List[update_version.types.ParserSpec]
        A list containing ``ParserSpec`` objects.

    Returns
    -------
    argparse.Namespace
        The generated ``argparse.Namespace`` object.
    """
    for spec in specs:
        opts, kwargs = spec["opts"], spec["kwargs"]
        parser.add_argument(*opts, **kwargs)

    try:
        namespace: Namespace = parser.parse_args()
    except ArgumentError:
        die(code=1, func=parser.print_usage)

    return namespace


def arg_parser_init(prog: str = "update-version") -> Tuple[ArgumentParser, Namespace]:
    """
    Generate the argparse namespace.

    Parameters
    ----------
    prog : str, optional, default="update-version"
        The program name.

    Returns
    -------
    parser : argparse.ArgumentParser
        The generated ``argparse.ArgumentParser`` object.
    namespace : argparse.Namespace
        The generated ``argparse.Namespace`` object.
    """
    parser = ArgumentParser(
        prog=prog,
        description="Update your project's version file",
        exit_on_error=False,
        formatter_class=ArgumentDefaultsHelpFormatter,
        add_help=True,
        allow_abbrev=True
    )
    spec: List[ParserSpec] = [
        ParserSpec(opts=["--input", "-i"], kwargs={
            "default": "./version.txt",
            "dest": "path",
            "metavar": "</path/to/file>",
            "nargs": 1,
            "required": False,
            "type": str
        }),
        ParserSpec(opts=["-v", "--verbose"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Enable verbose mode",
            "dest": "verbose",
        }),
        ParserSpec(opts=["-V", "--version"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Show version",
            "dest": "version",
        }),
        ParserSpec(opts=["-L", "--list-versions"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "List all versions of this script.",
            "dest": "list_versions",
        }),
        ParserSpec(opts=["-D", "--dry-run"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Don't modify the files, but do execute the rest",
            "dest": "dry_run",
        }),
        ParserSpec(opts=["--extra", "-e"], kwargs={
            "dest": "extra",
            "action": "store_true",
            "required": False,
        }),
        ParserSpec(opts=["--patch", "-p"], kwargs={
            "dest": "patch",
            "action": "store_true",
            "required": False,
        }),
        ParserSpec(opts=["--minor", "-m"], kwargs={
            "dest": "minor",
            "action": "store_true",
            "required": False,
        }),
        ParserSpec(opts=["--major", "-M"], kwargs={
            "dest": "major",
            "action": "store_true",
            "required": False,
        }),
        ParserSpec(opts=["--dashed", "-d"], kwargs={
            "dest": "dashed",
            "action": "store_true",
            "required": False,
        }),
        ParserSpec(opts=["--replace-with", "-r"], kwargs={
            "default": "",
            "dest": "replace",
            "metavar": "\"<MAJOR>.<MINOR>.<PATCH>[-<EXTRA>]\"",
            "nargs": 1,
            "required": False,
            "type": str,
        }),
    ]

    return parser, bootstrap_args(parser, spec)

# vim: set ts=4 sts=4 sw=4 et ai si sta:
