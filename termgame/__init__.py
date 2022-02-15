from sys import platform


class InvalidOS(Exception):
    """Raises if OS equals to Windows."""
    pass


if platform == 'win32':
    raise InvalidOS("TermGame library can't work on Windows.")

from .clock import Clock
from . import color
from . import draw
from . import events
from . import image
from . import pictures
from .screen import Screen

__version__ = 'beta 0.1.0'
