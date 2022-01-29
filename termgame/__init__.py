import sys


class InvalidOS(Exception): pass


if sys.platform == 'win32':
    raise InvalidOS("TermGame library can't work on Windows")

from .screen import Screen
from .draw import *

__version__ = 'alpha 0.1.0'
