# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Argument parsing utilities for ``update-version``.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "arg_parser_init",
    "bootstrap_args",
]

from argparse import ArgumentDefaultsHelpFormatter, ArgumentError, ArgumentParser, Namespace
from typing import List, Tuple

import argcomplete
from argcomplete.completers import FilesCompleter

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
    has_completer = False
    for spec in specs:
        opts, kwargs, completer = spec["opts"], spec["kwargs"], spec["completer"]
        if not completer or completer is None:
            parser.add_argument(*opts, **kwargs)
        else:
            has_completer = True
            parser.add_argument(*opts, **kwargs).completer = completer

    if has_completer:
        argcomplete.autocomplete(parser)

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
        }, completer=FilesCompleter(directories=False)),
        ParserSpec(opts=["--verbose", "-v"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Enable verbose mode",
            "dest": "verbose",
        }, completer=None),
        ParserSpec(opts=["--version", "-V"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Show version",
            "dest": "version",
        }, completer=None),
        ParserSpec(opts=["--print-version", "-P"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Print the current project's version",
            "dest": "print_version",
        }, completer=None),
        ParserSpec(opts=["--list-versions", "-L"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "List all versions of this script.",
            "dest": "list_versions",
        }, completer=None),
        ParserSpec(opts=["--dry-run", "-D"], kwargs={
            "required": False,
            "action": "store_true",
            "help": "Don't modify the files, but do execute the rest",
            "dest": "dry_run",
        }, completer=None),
        ParserSpec(opts=["--extra", "-e"], kwargs={
            "dest": "extra",
            "action": "store_true",
            "help": "Update the `extra` (_._._-X) component. This auto-enables `-d`",
            "required": False,
        }, completer=None),
        ParserSpec(opts=["--patch", "-p"], kwargs={
            "dest": "patch",
            "action": "store_true",
            "help": "Update the `patch` (_._.x[-_]) component",
            "required": False,
        }, completer=None),
        ParserSpec(opts=["--minor", "-m"], kwargs={
            "dest": "minor",
            "action": "store_true",
            "help": "Update the `minor` (_.x._[-_]) component",
            "required": False,
        }, completer=None),
        ParserSpec(opts=["--major", "-M"], kwargs={
            "dest": "major",
            "action": "store_true",
            "help": "Update the `major` (x._._[-_]) component",
            "required": False,
        }, completer=None),
        ParserSpec(opts=["--dashed", "-d"], kwargs={
            "dest": "dashed",
            "action": "store_true",
            "help": "Whether the version spec includes dashes",
            "required": False,
        }, completer=None),
        ParserSpec(opts=["--replace-with", "-r"], kwargs={
            "default": "",
            "dest": "replace",
            "help": "The custom version given by the user. Versions with a dash `-` require `-d`",
            "metavar": "\"<MAJOR>.<MINOR>.<PATCH>[-<EXTRA>]\"",
            "nargs": 1,
            "required": False,
            "type": str,
        }, completer=None),
    ]

    return parser, bootstrap_args(parser, spec)

# vim: set ts=4 sts=4 sw=4 et ai si sta:
