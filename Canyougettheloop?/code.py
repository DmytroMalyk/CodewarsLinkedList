def loop_size(node):
    nodes = set()
    current = node
    while current not in nodes:
        nodes.add(current)
        current = current.next
    c = current.next
    i = 1
    while c != current:
        i+=1
        c = c.next
    return i
