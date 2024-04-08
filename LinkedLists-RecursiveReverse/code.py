class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    current = head
    nxt = None
    while current:
        new = Node(current.data)
        new.next = nxt
        nxt = new
        current = current.next
    return nxt
