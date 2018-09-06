#!/usr/bin/env python

from pyfiglet import Figlet, figlet_format, print_figlet
import curses
from curses import (
    A_BOLD, 
    A_NORMAL,
    COLOR_RED,
    COLOR_BLACK,
    COLOR_GREEN,
    COLOR_YELLOW,
    COLOR_WHITE,
)

fig_large = Figlet(
    font="cyberlarge",
    justify="center",
)
fig_small = Figlet(
    font="cybersmall",
    justify="center",
)

def flushkeys(stdscr):
    try:
        while True:
            stdscr.getkey()
    except curses.error:
        pass

def main(stdscr):
    curses.curs_set(False)
    # curses.halfdelay(1)
    curses.init_pair(1, COLOR_GREEN, COLOR_BLACK)
    GREEN = curses.color_pair(1)
    curses.init_pair(2, COLOR_WHITE, COLOR_RED)
    ERROR = curses.color_pair(2) | A_BOLD
    curses.init_pair(3, COLOR_WHITE, COLOR_GREEN)
    SUCCESS = curses.color_pair(3) | A_BOLD
    while True:
        stdscr.bkgd(' ', 0)
        stdscr.clear()
        stdscr.addstr(4,0,fig_large.renderText(
            "Vector Display Initialized"
        ),GREEN|A_BOLD)
        stdscr.addstr(
            fig_small.renderText("AWAITING INPUT"),
            GREEN
        )
        stdscr.addstr("\n\n")
        stdscr.refresh()

        # Clear any kestrokes in the queue
        stdscr.getch()
        break

curses.wrapper(main)
print_figlet("Restart")
