# 40. Дано бинарное дерево. Найти высоту дерева.

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f'Value: {val}\nLeft: {left}\nRight: {right}'

def bin_tree_height(root) -> int:
    if root is None:
        return 0
    return 1 + max(bin_tree_height(root.left), bin_tree_height(root.right))

t1 = Node(5, Node(6, None, None), Node(7, None, None))
assert bin_tree_height(t1) == 2
t2 = Node(5, Node(6, Node(7, Node(8, Node(9, None, None), None), None, ), None), None)
assert bin_tree_height(t2) == 5
t3 = Node(5, Node(6, Node(7, Node(8, Node(9, None, None), None), None), None), t2)
assert bin_tree_height(t3) == 6
t4 = Node(5, Node(6, Node(7, t3, t3), None), t3)
assert bin_tree_height(t4) == 9
