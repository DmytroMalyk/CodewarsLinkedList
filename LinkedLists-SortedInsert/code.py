""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if data < head.data:
        res = Node(data)
        res.next = head
        return res
    curr = head
    while not (curr.data < data and curr.next is None) and \
        not (curr.data < data and curr.next.data > data):
        curr = curr.next
    res = Node(data)
    res.next = curr.next
    curr.next = res
    return head
