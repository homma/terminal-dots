
## edit.py

import curses

def update(app, n):
  y, x = app.win.getyx()
  app.data.update(x, y, n)
  c = app.data.get(x, y)
  app.win.addstr(y, x, c)
  # app.win.move(y, x)

def zero(app):
  update(app, 0)

def one(app):
  update(app, 1)

def two(app):
  update(app, 2)

def three(app):
  update(app, 3)

def four(app):
  update(app, 4)

def five(app):
  update(app, 5)

def six(app):
  update(app, 6)

def seven(app):
  update(app, 7)

def eight(app):
  update(app, 8)

def nine(app):
  update(app, 9)

