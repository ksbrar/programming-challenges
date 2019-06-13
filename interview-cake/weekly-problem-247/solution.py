class LinkedListNode(object):
  def __init__(self, value):
    self.value = value
    self.next = None

def printLL(start):
  while(start != None):
    print(start.value, end=" -> ")
    start = start.next
  print('END')

def delete_node(n):
  if n.next == None:
    n.value = None
  else:
    n.value = n.next.value
    n.next = n.next.next

def main():
  a = LinkedListNode('A')
  b = LinkedListNode('B')
  c = LinkedListNode('C')

  start = a
  a.next = b
  b.next = c
  
  printLL(start)

  delete_node(b)

  printLL(start)

if __name__ == "__main__":
  main()
