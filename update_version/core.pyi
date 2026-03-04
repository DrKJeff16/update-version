from .args.parsing import arg_parser_init as arg_parser_init
from .util import die as die
from .util import verbose_print as verbose_print
from .version import __version__ as __version__
from .version import list_versions as list_versions
from .version import version_print as version_print

PATH: str

def convert_to_version(data: str, dashed: bool) -> list[int]:
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
def retrieve_version(path: str, dashed: bool) -> list[int]:
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
def gen_version_str(version: list[int] | list[str], dashed: bool) -> str:
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
def main() -> int:
    """
    Execute the script.

    Returns
    -------
    int
        The exit code.
    """

# vim: set ts=4 sts=4 sw=4 et ai si sta:
