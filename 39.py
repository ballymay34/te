# 39. Дано бинарное дерево. Проверить является ли данное дерево бинарным деревом поиска.

# ejudge: https://www.geeksforgeeks.org/problems/check-for-bst/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
def isBST(root, less=float('inf'), greater=float('-inf')):
    if root is None:
        return True
    if not (greater <= root.data < less):
        return False
    return isBST(root.left, root.data, greater) and isBST(root.right, less, root.data)

class Solution:
    def isBST(self, root):
        return isBST(root)
