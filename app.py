#!/usr/bin/env python

## app.py

import curses
import locale

import key_event
import key_move
import model
import edit
import copy

# global data holder
class App():
  def __init__(self):
    self.win = curses.initscr()
    self.setup_window()
    h, w = self.win.getmaxyx()
    self.data = model.Model(w, h)

  def setup_window(self):
    curses.curs_set(False)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, -1, -1)
    self.win.bkgd(' ', curses.color_pair(1))
  
  # event loop
  def loop(self):
    while True:
      key = self.win.getkey()
      key_event.do_key_action(self, key)
  
  def quit_app(self, args):
    curses.nocbreak(); self.win.keypad(0); curses.echo()
    curses.endwin()
    self.data.dump()
    quit()

def add_event(app):
  # cursor moves
  key_event.add_key_action('k', key_move.up)
  key_event.add_key_action('j', key_move.down)
  key_event.add_key_action('H', key_move.top)
  key_event.add_key_action('L', key_move.bottom)
  key_event.add_key_action('h', key_move.left)
  key_event.add_key_action('l', key_move.right)
  key_event.add_key_action('J', key_move.left_end)
  key_event.add_key_action('a', key_move.left_end)
  key_event.add_key_action('K', key_move.right_end)
  key_event.add_key_action('e', key_move.right_end)
  
  # data modification
  key_event.add_key_action('0', edit.zero)
  key_event.add_key_action('1', edit.one)
  key_event.add_key_action('2', edit.two)
  key_event.add_key_action('3', edit.three)
  key_event.add_key_action('4', edit.four)
  key_event.add_key_action('5', edit.five)
  key_event.add_key_action('6', edit.six)
  key_event.add_key_action('7', edit.seven)
  key_event.add_key_action('8', edit.eight)
  key_event.add_key_action('9', edit.nine)
  
  # copy, paste
  key_event.add_key_action('y', copy.copy)
  key_event.add_key_action('p', copy.paste)
  
  # quit
  key_event.add_key_action('q', app.quit_app)

def main(args):
  app = App()
  add_event(app)  
  app.loop()

# set locale before initialize curses
locale.setlocale(locale.LC_ALL, "")

curses.wrapper(main)

