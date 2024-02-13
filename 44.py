# 44. Дано бинарное дерево поиска. Найти все тупиковые узлы. Под тупиковым узлом понимается узел, добавление потомков к которому невозможно.

# ejudge: https://practice.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
class Solution:
    def isDeadEnd(self, root):
        deadends = []
        def dfs(a, smaller, greater):
            if a is None:
                return
            if a.data - 1 == greater and a.data + 1 == smaller:
                deadends.append(a.data)
            dfs(a.left, a.data, greater)
            dfs(a.right, smaller, a.data)
        dfs(root, float('inf'), 0)
        return deadends

