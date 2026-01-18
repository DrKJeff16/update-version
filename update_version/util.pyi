from typing import Callable, TextIO

__all__ = ['die', 'error', 'verbose_print']

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
def die(*msg, code: int = 0, func: Callable[[TextIO], None] | None = None, **kwargs) -> None:
    '''
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
    '''
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

# vim: set ts=4 sts=4 sw=4 et ai si sta:
