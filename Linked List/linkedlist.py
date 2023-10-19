from node import node

list = node("world")
list.setNext(node("hello"))

print(list.getData())
print(list.getNext().getData())
