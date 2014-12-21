
## key_event.py

import curses

key_actions = dict()

def add_key_action(key, fun):
  if key in key_actions:
    actions = key_actions[key]
    actions.append(fun)
  else:
    key_actions[key] = [fun]

def do_key_action(app, key):
  if key not in key_actions:
    return
  
  actions = key_actions[key]
  for fun in actions:
    fun(app)

