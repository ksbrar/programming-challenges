# Delete Node

Description: Delete a node from a singly-linked list, given *only* a variable pointing to that node.

Example (python3): Given the input **b** below:
```python
class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
```

[Original link](https://www.getdrip.com/deliveries/92m6yfma2wbrevwvwdrq?utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23247%3A%20Delete%20Node&utm_medium=email&utm_source=drip).
