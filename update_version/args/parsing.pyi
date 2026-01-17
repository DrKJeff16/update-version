from argparse import ArgumentParser, Namespace

from ..types import ParserSpec

__all__ = ['arg_parser_init', 'bootstrap_args']

def bootstrap_args(parser: ArgumentParser, specs: list[ParserSpec]) -> Namespace:
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
def arg_parser_init(prog: str = 'update-version') -> tuple[ArgumentParser, Namespace]:
    '''
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
    '''

# vim: set ts=4 sts=4 sw=4 et ai si sta:
