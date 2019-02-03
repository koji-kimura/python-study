# coding: UTF-8
class Orange:
  def __init__(self,w,c):
    self.weight= w
    self.color= c
    self.mold = 0
    print("created")
  def rot(self,days,temp):
    """tep(湿度)は摂氏"""
    self.mold = days*temp

or1= Orange(10,"dark orange")
print(or1.mold)
or1.rot(10,37)
print(or1.mold)
# print(or1.weight)
# print(or1.color)

# or1.weight = 100
# or1.color = "light orange"
# print(or1.weight)
# print(or1.color)

# or2= Orange(30,"dark orange")
# or3= Orange(20,"yellow")
