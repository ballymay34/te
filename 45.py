# 45. Дан корень бинарного дерева. Необходимо преобразовать дерево в односвязный список.
#     Список должен использовать тот же класс `Node`, правый указатель должен ссылаться на следующий элемент в списке, левый всегда `None`.
#     Список должен иметь тот же порядок, что и прямой обход бинарного дерева.

def tree_to_list(root):
    ll_start = Node(None, None, None)
    ll_end = ll_start
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        if not node.left and not node.right:
            ll_end.right = Node(node.val, None, None)
            ll_end = ll_end.right
        else:
            stack.append(Node(node.val))
    return ll_start.right

t = Node('F', Node('B', Node('A'), Node('D', Node('C'), Node('E'))), Node('G', None, Node('I', Node('H'), None)))
print(tree_to_list(t))