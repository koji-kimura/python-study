class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def pop(self):
    return self.items.pop()

  def push(self,item):
    self.items.append(item)

  def peek(self):
    last = len(self.items)-1
    return self.items[last]
  
  def size(self):
    return len(self.items)

stack = Stack()
for c in "yesterday":
  stack.push(c)

reverse = ""

while stack.size():
  reverse+= stack.pop()

print(reverse)

stack2 = Stack()
for c2 in [1,2,3,4,5]:
  stack2.push(c2)

reverse2 = []
for i in range(len(stack2.items)):
    reverse2.append(stack2.pop())

print(reverse2)