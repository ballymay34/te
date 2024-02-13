# 37. Дано бинарное дерево. Выполнить прямой/центрированный/обратный/уровневый обход дерева.

# source: https://ru.wikipedia.org/wiki/Обход_дерева
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f'Value: {val}\nLeft: {left}\nRight: {right}'

def nlr(node): # прямой
    if node is None: return
    print(node.val, end='')
    nlr(node.left)
    nlr(node.right)

def lnr(node): # центрированный
    if node is None: return
    lnr(node.left)
    print(node.val, end='')
    lnr(node.right)

def lrn(node): # обратный
    if node is None: return
    lrn(node.left)
    lrn(node.right)
    print(node.val, end='')

def dfs_level(root): # уровневый, через обход в ширину
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None: continue
        print(node.val, end='')
        queue.append(node.left)
        queue.append(node.right)


t = Node('F', Node('B', Node('A'), Node('D', Node('C'), Node('E'))), Node('G', None, Node('I', Node('H'), None)))
nlr(t)
print()
lnr(t)
print()
lrn(t)
print()
dfs_level(t)