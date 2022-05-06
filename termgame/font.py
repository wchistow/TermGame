# Constants for different kinds of font.
BOLD = '\033[0;1m'
HALF_BOLD = '\033[0;2m'
ITALICS = '\033[0;3m'
UNDERLINED = '\033[0;4m'
FLASHING = '\033[0;5m'  # or '\033[0;6m'
DEDICATED = '\033[0;7m'
INVISIBLE = '\033[0;8m'
CROSSED_OUT = '\033[0;9m'
RESET_FONT = '\033[0m'


def join(symbol: str, font: str) -> str:
    """Return arg1 + symbol"""
    if not font:
        return font + symbol
    else:
        return font + symbol + RESET_FONT
