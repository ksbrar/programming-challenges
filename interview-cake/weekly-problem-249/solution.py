class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k, node):
  pass

def main():
  a = LinkedListNode('Angel Food')
  b = LinkedListNode('Bundt')
  c = LinkedListNode('Cheese')
  d = LinkedListNode('Devil\'s Food')
  e = LinkedListNode('Eccles')

  a.next = b
  b.next = c
  c.next = d
  d.next = e

  kth_to_last_node(2, a)

if __name__ == "__main__":
  main()
