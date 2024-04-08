def linked_list_from_string(s):
    if s == 'None':
        return None
    head = Node(int(s.split(' -> ')[0]))
    curr = head
    for el in s.split(' -> ')[1:]:
        if el == 'None':
            return head
        curr.next = Node(int(el))
        curr = curr.next
    return head
