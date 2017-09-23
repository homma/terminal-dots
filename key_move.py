
## key_move.py

import curses

def up(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  if y != 0:
    app.win.move(y - 1, x)
  app.win.chgat(1, curses.A_UNDERLINE)

def down(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_y = h - 1
  if y < max_y:
    app.win.move(y + 1, x)
  app.win.chgat(1, curses.A_UNDERLINE)

def top(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  app.win.move(0, x)
  app.win.chgat(1, curses.A_UNDERLINE)

def bottom(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_y = h - 1
  app.win.move(max_y, x)
  app.win.chgat(1, curses.A_UNDERLINE)

def left(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  if x != 0:
    app.win.move(y, x - 1)
  app.win.chgat(1, curses.A_UNDERLINE)

def right(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_x = w - 1
  if x < max_x:
    app.win.move(y, x + 1)
  app.win.chgat(1, curses.A_UNDERLINE)

def right_end(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_x = w - 1
  app.win.move(y, max_x)
  app.win.chgat(1, curses.A_UNDERLINE)

def left_end(app):
  app.win.chgat(1, curses.A_NORMAL)
  y, x = app.win.getyx()
  app.win.move(y, 0)
  app.win.chgat(1, curses.A_UNDERLINE)

