from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    curr = node
    num = 0
    while curr:
        if num == index:
            return curr
        num += 1
        curr = curr.next
    raise ValueError()
