
## model.py

import sys

class Model():
  data = []
  
  dot_base = int("2800", 16)
  dot_zero = 0
  dot_full = 255
  pattern = [0, 1, 2, 4, 8, 16, 32, 64, 128, 255]
  
  def __init__(self, w, h):
    for i in range(h):
      self.data.append(bytearray(w))
  
  def update(self, x, y, num):
    current = self.data[y][x]
    if num == 0:
      result = self.dot_zero
    elif num == 9:
      result = self.dot_full
    else:
      modifier = self.pattern[num]
      result = current ^ modifier
    self.data[y][x] = result
  
  def num_to_char(self, n):
    return unichr(self.dot_base + n).encode('utf-8')
    # return unichr(self.dot_base + n)
  
  def get(self, x, y):
    n = self.data[y][x]
    return self.num_to_char(n)
  
  def dump(self):
    for i in range(len(self.data)):
      for j in range(len(self.data[i])):
        c = self.get(j, i)
        sys.stdout.write(c)
  
  def data_export(self):
    pass
  
  def data_import(self):
    pass

