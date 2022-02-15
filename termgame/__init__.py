from sys import platform


class InvalidOS(Exception):
    """Raises if OS equals to Windows."""
    pass


if platform == 'win32':
    raise InvalidOS("TermGame library can't work on Windows.")

from .screen import Screen
from . import draw
from . import color
from . import events
from . import image
from .clock import Clock
from . import pictures

__version__ = 'beta 0.1.0'
