# -*- coding: utf-8 -*-

from typing import Final


# fg
BLACK: Final[str] = '\033[30m'          # Black
RED: Final[str] = '\033[31m'            # Red
GREEN: Final[str] = '\033[32m'          # Green
YELLOW: Final[str] = '\033[33m'         # Yellow
BLUE: Final[str] = '\033[34m'           # Blue
MAGENTA: Final[str] = '\033[35m'        # Magenta
CYAN: Final[str] = '\033[36m'           # Cyan
WHITE: Final[str] = '\033[37m'          # White
COLOR_DEFAULT: Final[str] = '\033[39m'  # Return to default the text color

# the text
BOLD: Final[str] = '\033[1m'            # Bold
UNDERLINE: Final[str] = '\033[4m'       # Under line
INVISIBLE: Final[str] = '\033[08m'      # Invisible
REVERCE: Final[str] = '\033[07m'        # Reverse the text color and back ground color

# bg
BG_BLACK: Final[str] = '\033[40m'       # Black
BG_RED: Final[str] = '\033[41m'         # Red
BG_GREEN: Final[str] = '\033[42m'       # Green
BG_YELLOW: Final[str] = '\033[43m'      # Yellow
BG_BLUE: Final[str] = '\033[44m'        # Blue
BG_MAGENTA: Final[str] = '\033[45m'     # Magenta
BG_CYAN: Final[str] = '\033[46m'        # Cyan
BG_WHITE: Final[str] = '\033[47m'       # White
BG_DEFAULT: Final[str] = '\033[49m'      # Return to default back ground color

RESET: Final[str] = '\033[0m'           # All reset

def options(text: str, bold: bool, line: bool, \
            invisible: bool, reverce: bool) -> str:
    if bold:
        text = BOLD + text
    if line:
        text = UNDERLINE + text
    if invisible:
        text = INVISIBLE + text
    if reverce:
        text = REVERCE

    return text
    

def black(text: str, *, bold: bool = False, line: bool = False, \
            invisible: bool = False, reverce: bool = False) -> str:

    return BLACK + options(text, bold, line, invisible, reverce) + RESET

def red(text: str) -> str:
    return RED + text + RESET

def green(text: str) -> str:
    return GREEN + text + RESET

