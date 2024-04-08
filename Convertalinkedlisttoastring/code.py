def stringify(node):
    res = ''
    curr = node
    if not curr:
        return 'None'
    while curr:
        res += str(curr.data) + ' -> '
        curr = curr.next
    return res + 'None'
