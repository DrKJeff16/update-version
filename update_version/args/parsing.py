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

from argparse import ArgumentError, ArgumentParser, Namespace
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
        opts, kwargs, completer = spec.opts, spec.kwargs, spec.completer
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
        die(code=1, func=parser.print_help)

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
        add_help=True,
        allow_abbrev=True
    )
    spec: List[ParserSpec] = [
        ParserSpec(
            "path",
            completer=FilesCompleter(directories=False),
            default="./version.txt",
            help="The path to the versioning file. Defaults to `./version.txt`",
            nargs="?"
        ),
        ParserSpec(
            "--verbose",
            "-v",
            action="store_true",
            dest="verbose",
            help="Enable verbose mode",
            required=False
        ),
        ParserSpec(
            "--version",
            "-V",
            action="store_true",
            dest="version",
            help="Show version",
            required=False
        ),
        ParserSpec(
            "--print-version",
            "-P",
            action="store_true",
            dest="print_version",
            help="Print the current project's version",
            required=False
        ),
        ParserSpec(
            "--list-versions",
            "-L",
            action="store_true",
            dest="list_versions",
            help="List all versions of this script.",
            required=False
        ),
        ParserSpec(
            "--dry-run",
            "-D",
            action="store_true",
            dest="dry_run",
            help="Don't modify the files, but do execute the rest",
            required=False
        ),
        ParserSpec(
            "--extra",
            "-e",
            action="store_true",
            dest="extra",
            help="Update the extra `N` (X.Y.Z-N) component. This auto-enables `-d`",
            required=False
        ),
        ParserSpec(
            "--patch",
            "-p",
            action="store_true",
            dest="patch",
            help="Update the patch `Z` (X.Y.Z[-N]) component",
            required=False
        ),
        ParserSpec(
            "--minor",
            "-m",
            action="store_true",
            dest="minor",
            help="Update the minor `Y` (X.Y.Z[-N]) component",
            required=False
        ),
        ParserSpec(
            "--major",
            "-M",
            action="store_true",
            dest="major",
            help="Update the major `X` (X.Y.Z[-N]) component",
            required=False
        ),
        ParserSpec(
            "--dashed",
            "-d",
            action="store_true",
            dest="dashed",
            help="Whether the version spec includes dashes",
            required=False
        ),
        ParserSpec(
            "--replace-with",
            "-r",
            default="",
            dest="replace",
            help="The custom version given by the user. Versions with a dash `-` require `-d`",
            metavar="\"<MAJOR>.<MINOR>.<PATCH>[-<EXTRA>]\"",
            nargs=1,
            required=False,
            type=str,
        ),
    ]

    return parser, bootstrap_args(parser, spec)

# vim: set ts=4 sts=4 sw=4 et ai si sta:
