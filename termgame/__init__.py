from sys import platform


class InvalidOS(Exception):
    pass


if platform == 'win32':
    raise InvalidOS("TermGame library can't work on Windows.")

from .screen import Screen
from . import draw
from . import color
from . import events
from . import image
from .clock import Clock

__version__ = 'alpha 0.1.0'
