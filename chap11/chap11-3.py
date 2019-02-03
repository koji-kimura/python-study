# coding: UTF-8
class Reactangle:
  def __init__(self,w,l):
    self.width = w
    self.len = 1
  
  def area(self):
    return self.width*self.len
  
  def change_size(self,w,l):
    self.width = w
    self.len = 1

rectagle = Reactangle(10,20)
print(rectagle.area())
rectagle.change_size(20,40)
print(rectagle.area())
