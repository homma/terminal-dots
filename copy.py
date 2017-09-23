
## copy.py

import curses

clip = ""

def copy(app):
  y, x = app.win.getyx()
  global clip
  clip = app.data.get_char(x, y)

def paste(app):
  y, x = app.win.getyx()
  if clip:
    app.data.update_cell_char(x, y, clip)
  app.win.addstr(y, x, clip)

