from node import Node
# Create the Queue class below:
class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
#devuelva el valor de la cabeza de la pila usando el método get_value() de Node.
  def peek(self):
    return self.head.get_value()