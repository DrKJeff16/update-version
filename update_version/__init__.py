# PYTHON_ARGCOMPLETE_OK
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
Version updater from a target file.

Copyright (c) 2026 Guennadi Maximov C. All Rights Reserved.
"""
__all__ = [
    "ParserSpec",
    "VersionInfo",
    "__version__",
    "args",
    "update",
    "util",
    "version",
]

from . import args, update, util, version
from .types import ParserSpec, VersionInfo

__version__: str = version.__version__

# vim: set ts=4 sts=4 sw=4 et ai si sta:
