# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Version updater utilities.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "die",
    "error",
    "verbose_print",
]

import sys
from sys import stderr, stdout
from typing import Callable, TextIO


def error(*msg, **kwargs) -> None:
    """
    Print to stderr.

    Parameters
    ----------
    *msg
        The data to be printed to stderr.
    **kwargs
        Extra arguments for the ``print()`` function (``end``, ``sep`` and ``flush``).
    """
    end: str = kwargs.get("end", "\n")
    sep: str = kwargs.get("sep", " ")
    flush: bool = kwargs.get("flush", False)
    print(*msg, file=stderr, end=end, sep=sep, flush=flush)


def die(*msg, code: int = 0, func: Callable[[TextIO], None] | None = None, **kwargs) -> None:
    """
    Kill the program execution.

    Summons ``sys.exit()`` with a provided code and optionally prints code to stderr or stdout
    depending on the provuded exit code.

    Parameters
    ----------
    *msg : optional
        Data to be printed.
    code : int, default=0
        The exit code.
    func : Callable[[TextIO], None], optional
        A function to be called with a TextIO object if provided.
    **kwargs
        Extra arguments for the ``print()`` function (``end``, ``sep`` and ``flush``).

    Examples
    --------
    To kill the program with code 0 without any message.

    >>> from update_version.util import die
    >>> die(code=0)

    To kill the program with non-zero exit code with message (will print to stderr).

    >>> from update_version.util import die
    >>> die("foo", "bar", code=1)
    foo bar

    To kill the program with exit code 0 with message (will print to stdout).

    >>> from update_version.util import die
    >>> die("foo", "bar")
    foo bar
    """
    try:
        code = int(code)
    except Exception:
        code = 1

    if func is not None and callable(func):
        func(stderr if code != 0 else stdout)

    if msg and len(msg) > 0:
        if code == 0:
            print(*msg, **kwargs)
        else:
            error(*msg, **kwargs)

    sys.exit(code)


def verbose_print(*msg, verbose: bool, **kwargs) -> None:
    """
    Only prints the given data if verbose mode is activated.

    Parameters
    ----------
    *msg
        Data to be printed.
    verbose : bool
        Flag to signal whether to execute this function or not.
    **kwargs
        Extra arguments for the ``print()`` function (``end``, ``sep`` and ``flush``).
    """
    if not verbose:
        return

    end: str = kwargs.get("end", "\n")
    sep: str = kwargs.get("sep", " ")
    flush: bool = kwargs.get("flush", False)

    print(*msg, end=end, sep=sep, flush=flush)

# vim: set ts=4 sts=4 sw=4 et ai si sta:
