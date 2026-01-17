from .args.parsing import arg_parser_init as arg_parser_init
from .util import die as die

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
def main() -> int:
    """
    Execute the script.

    Returns
    -------
    int
        The exit code.
    """
