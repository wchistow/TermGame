import sys


class InvalidOS(Exception): pass


if sys.platform == 'win32':
    raise InvalidOS("TermGame library can't work on Windows")

from .game import Game

__version__ = '0.1.0'
