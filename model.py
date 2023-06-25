# -*- coding: utf-8 -*-
## model.py

import sys

class Model():
  # array of dot data
  # data[y][x]
  data = []
  
  dot_base = int("2800", 16)
  dot_zero = 0
  dot_full = 255
  pattern = [0, 1, 2, 4, 8, 16, 32, 64, 128, 255]
  
  def __init__(self, w, h):
    for i in range(h):
      self.data.append(bytearray(w))
  
  # update cell with a unicode charactor
  # register undo here (to be implemented)
  def update_cell_char(self, x, y, ch):
    self.data[y][x] = self.char_to_num(ch)
  
  # update cell by a number
  # register undo here (to be implemented)
  def update_cell_num(self, x, y, num):
    self.data[y][x] = num
  
  # update by each dot
  def update_dot(self, x, y, num):
    current = self.get_num(x, y)
    if num == 0:
      result = self.dot_zero
    elif num == 9:
      result = self.dot_full
    else:
      modifier = self.pattern[num]
      result = current ^ modifier
    self.update_cell_num(x, y, result)
  
  def char_to_num(self, c):
    return ord(c) - self.dot_base
  
  def num_to_char(self, n):
    return chr(self.dot_base + n)
  
  def get_num(self, x, y):
    return self.data[y][x]
  
  def get_char(self, x, y):
    n = self.data[y][x]
    return self.num_to_char(n)
  
  def dump(self):
    # print "#" * 80
    # sys.stdout.write("\033[2J")
    # sys.stdout.write("\033[0;0H")
    for i in range(len(self.data)):
      for j in range(len(self.data[i])):
        c = self.get_char(j, i)
        sys.stdout.write(c)
      sys.stdout.write("\n")
    # print "#" * 80
  
  # exporter : to be implemented
  def data_export(self):
    pass
  
  # importer : to be implemented
  def data_import(self):
    pass

# test code
if __name__ == '__main__':
  model = Model(80, 24)
  ch = model.num_to_char(model.dot_full)
  print(ch)
  num = model.char_to_num(ch)
  print(num)

