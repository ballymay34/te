# 38. Дано бинарное дерево. Проверить является ли данное дерево сбалансированным.

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f'Value: {val}\nLeft: {left}\nRight: {right}'

def bin_tree_height(root) -> int: # from task #40
    if root is None:
        return 0
    return 1 + max(bin_tree_height(root.left), bin_tree_height(root.right))

def is_balanced_bin_tree(root) -> bool:
    if root is None:
        return True
    return abs(bin_tree_height(root.left) - bin_tree_height(root.right)) <= 1

t1 = Node(1, Node(1, None, None), Node(1, None, None))
assert is_balanced_bin_tree(t1) == True
t2 = Node(1, t1, t1)
assert is_balanced_bin_tree(t2) == True
t3 = Node(1, t1, None)
assert is_balanced_bin_tree(t3) == False
t4 = Node(1, t3, t1)
assert is_balanced_bin_tree(t4) == True
t5 = Node(1, t4, t1)
assert is_balanced_bin_tree(t5) == False
