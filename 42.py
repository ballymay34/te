# 42. Дано бинарное дерево поиска. Реализовать функцию поиска/вставки/удаления узла.

def find(node, x):
    if node is None:
        return False
    if node.val == x:
        return True
    return find(node.left, x) if x < node.val else find(node.right, x)

def insert(node, x):
    if x <= node.val
        if node.left is None:
            node.left = x
        else:
            insert(node.left, x)
    else:
        if node.right is None:
            node.right = x
        else:
            insert(node.right, x)

def delete(node, x):
    if node is None:
        return None
    if x < node.val:
        node.left = delete(node.left, x)
        return
    elif x > node.val:
        node.right = delete(node.right, x)
        return
    if node.left is None:
        temp = root.right
        root = None
        return temp
    elif node.right is None:
        temp = root.left
        root = None
        return temp
    # complex case: we need to remove a node that has 2 children
    # search for next bigger element, place its value in place of current node, delete its previous location
    next = root.right
    while next.left is not None:
        next = next.left
    node.val = next.val
    node.right = delete(node.right, node.val)

