
## key_move.py

import curses

def up(app):
  y, x = app.win.getyx()
  if y != 0:
    app.win.move(y - 1, x)

def down(app):
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_y = h - 1
  if y < max_y:
    app.win.move(y + 1, x)

def top(app):
  y, x = app.win.getyx()
  app.win.move(0, x)

def bottom(app):
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_y = h - 1
  app.win.move(max_y, x)

def left(app):
  y, x = app.win.getyx()
  if x != 0:
    app.win.move(y, x - 1)

def right(app):
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_x = w - 1
  if x < max_x:
    app.win.move(y, x + 1)

def right_end(app):
  y, x = app.win.getyx()
  h, w = app.win.getmaxyx()
  max_x = w - 1
  app.win.move(y, max_x)

def left_end(app):
  y, x = app.win.getyx()
  app.win.move(y, 0)

