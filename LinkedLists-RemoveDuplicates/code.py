class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None
    curr = head
    nodes = {curr.data}
    while curr.next:
        if curr.next.data in nodes:
            curr.next = curr.next.next
        else:
            nodes.add(curr.next.data)
            curr = curr.next
    return head
