#!/usr/bin/env python

## app.py

import curses
import locale

import key_event
import key_move
import model
import edit

# global data holder
class App():
  def __init__(self, win, data):
    self.win = win
    self.data = data
  
  def quit_app(self, args):
    curses.nocbreak(); self.win.keypad(0); curses.echo()
    curses.endwin()
    self.data.dump()
    quit()

def init():
  curses.curs_set(1)  # doesn't work on some environment
  win = curses.initscr()
  h, w = win.getmaxyx()
  data = model.Model(w, h)
  app = App(win, data)
  add_event(app)  
  return(app)

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
  
  # quit
  key_event.add_key_action('q', app.quit_app)

def loop(app):
  while True:
    key = app.win.getkey()
    key_event.do_key_action(app, key)

def main(args):
  app = init()
  loop(app)

locale.setlocale(locale.LC_ALL, "")
curses.wrapper(main)

