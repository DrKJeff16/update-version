__all__ = ['convert_to_version', 'gen_new_version', 'gen_version_str', 'main', 'retrieve_version']

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
def gen_new_version(old_version: list[int], replace: list[int], components: tuple[bool, bool, bool, bool]) -> list[str]:
    """
    Generate new version list.

    Parameters
    ----------
    old_version : List[int]
        The old version parsed as a list of integers.
    replace : List[int]
        The replaced version as a list of integers.
    components : Tuple[bool, bool, bool, bool]
        A tuple of booleans signaling, in order, the major, minor, patch and extra components.

    Returns
    -------
    List[str]
        A list of strings, each element is a version component, in order.
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
