# Дано бинарное дерево. Выполнить прямой/центрированный/обратный обход дерева не используя рекурсию.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f'Value: {self.val}\nLeft: {self.left}\nRight: {self.right}'

def nlr(node): # прямой
    if node is None: return
    stack = [node]
    while stack:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        if not node.left and not node.right:
            print(node.val, end='')
        else:
            stack.append(Node(node.val))

def lnr(node): # центрированный
    if node is None: return
    stack = [node]
    while stack:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if not node.left and not node.right:
            print(node.val, end='')
        else:
            stack.append(Node(node.val))
        if node.left is not None:
            stack.append(node.left)

def lrn(node): # обратный
    stack = [node]
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            print(node.val, end='')
        else:
            stack.append(Node(node.val))
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

t = Node('F', Node('B', Node('A'), Node('D', Node('C'), Node('E'))), Node('G', None, Node('I', Node('H'), None)))
nlr(t)
print()
lnr(t)
print()
lrn(t)