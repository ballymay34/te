# 20. Дан односвязный список. Определить содержит ли он цикл. Список может содержать петли.


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def __str__(self):
        return f'{self.val} {self.next}'

def has_cycle(node):
    visited = set()
    while node.next:
        if node.next == node:
            return False # has a loop in a single node, according to the task it's ok
        if node.next in visited:
            return True
        node = node.next
        visited.add(node)
    return False


print(has_cycle(Node(12, Node(9, Node(7, Node(5, None))))))
n = Node(12, None)
n.next = n
print(has_cycle(n))
n2 = Node(1, Node(2, Node(3, None)))
n2.next.next.next = n2 # add a cycle
print(has_cycle(n2))