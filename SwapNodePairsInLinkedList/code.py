from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    prev = None
    curr = head
    while curr and curr.next:
        next_iteration = curr.next.next
        second_node = curr.next
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        curr.next = second_node.next
        second_node.next = curr
        
        prev = curr
        curr = next_iteration
    return head
