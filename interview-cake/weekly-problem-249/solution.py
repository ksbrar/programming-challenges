class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

'''
Both methods below are O(n), though the first requires two walks through the
list of nodes (my solution) and the second uses two pointers to perform only
one walk (second of two solutions provided by Interview Cake, more clever IMO).
'''
def kth_to_last_node(k, node):
  # Count list length:
  list_length = 0
  n = node
  while (n != None):
    n = n.next
    list_length += 1
  
  # Break if list too short:
  if list_length < k or k == 0:
    print('k out of bounds!')
    return
  
  # Otherwise find the (len-k)th node:
  kn = node
  for _ in range(list_length-k):
    kn = kn.next
  print('Kth node: ' + kn.value)

def kth_to_last_node_2(k, node):
  # Initialize walkers:
  ln = node
  rn = node
  if (k == 0):
    print('k out of bounds!')
    return 

  for _ in range(k):
    if (rn == None):
      print('k out of bounds!')
      return
    rn = rn.next
  
  while (rn != None):
    ln = ln.next
    rn = rn.next
  print('Kth node: ' + ln.value)

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
  kth_to_last_node_2(2, a)

if __name__ == "__main__":
  main()
