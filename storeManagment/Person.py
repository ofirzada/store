
from . import config
class Person:
  def __init__(self, name, id,temp,hasMask,needIsolate):
    self.name = name
    self.id = id
    self.temp=temp
    self.hasMask=hasMask
    self.needIsolate = needIsolate
  def isSafe(self):
    return self.hasMask and not self.needIsolate and self.temp < config.UnhealthyTemp
