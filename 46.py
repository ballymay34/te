# 46. Дано представление полного бинарного дерева в виде списка. Необходимо построить бинарное дерево.

# ejudge: https://practice.geeksforgeeks.org/problems/make-binary-tree/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
from collections import deque
def convert(head):
    tree = Tree(head.data)
    level = deque([tree])
    while level:
        node = level.popleft()
        if head.next:
            node.left = Tree(head.next.data)
            head = head.next
            level.append(node.left)
        if head.next:
            node.right = Tree(head.next.data)
            head = head.next
            level.append(node.right)
    return tree
