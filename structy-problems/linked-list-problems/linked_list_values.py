# Write a function, linked_list_values, that takes in the head of a
# linked lists as an argument. The function should return a list
# conaining all values of the nodes in the linked list.

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def linked_list_values(head):
    current = head
    values = []
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

a = Node('a')
b = Node('b')
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_values(a))