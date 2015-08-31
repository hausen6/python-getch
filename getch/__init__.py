#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from msvc import *
except (ImportError):
    from getch import (atexit, set_normal_term, set_curses_term,
        putch, getch, getche, kbhit)
