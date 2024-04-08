from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)
