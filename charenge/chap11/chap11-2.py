import math
class Shape():
  def what_am_i(self):
    print("I am a shape")

class Circle(Shape):
  def __init__(self.s1)
    self.s1 = s1
  def area(self.s1)
    return s1*s1*math.pi

class Square(Shape):
  square_list = []
  def __init__(self,s1):
    self.s1 = s1
    self.square_list.append(self)
  
  def calculate_perimeter(self):
    return self.s1 *4
  
  def what_am_i(self):
    super().what_am_i()
    print("I am a square")
  
  def __repr__(self):
      return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
a_circle = Circle(2)
print(a_square)
print(a_circle.area)