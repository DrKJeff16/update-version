from . import args as args
from . import update as update
from . import util as util
from . import version as version
from .types import ParserSpec as ParserSpec
from .types import VersionInfo as VersionInfo

__all__ = ['ParserSpec', 'VersionInfo', '__version__', 'args', 'update', 'util', 'version']

__version__: str

# vim: set ts=4 sts=4 sw=4 et ai si sta:
