# 41. Дано бинарное дерево. Найти ширину дерева.

def get_max_width(root):
    max_width = 0
    level = [root]
    while level:
        max_width = max(max_width, len(level))
        new_level = []
        while level:
            node = level.pop()
            if node.right is not None:
                new_level.append(node.right)
            if node.left is not None:
                new_level.append(node.left)
        level = new_level[::-1]
    return max_width