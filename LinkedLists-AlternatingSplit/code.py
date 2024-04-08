class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError()
    first_curr = None
    second_curr = None
    frst = True
    curr = head
    while curr:
        if frst:
            if not first_curr:
                first = curr
                first_curr = curr
            else:
                first_curr.next = curr
            first_curr = curr
        else:
            if not second_curr:
                second = curr
                second_curr = curr
            else:
                second_curr.next = curr
            second_curr = curr
        frst = not frst
        curr = curr.next
    if first_curr:
        first_curr.next = None
    if second_curr:
        second_curr.next = None
    return Context(first, second)
