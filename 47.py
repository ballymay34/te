# 47. Дано бинарное дерево поиска с целочисленными ключами. Найти преемника и предшественника данного ключа `key`. Если какого-то значения не существует, верните вместо него `None`.

#    *Примечание:* преемник и предшественник - ближайшие значения после и до указанного ключа.

# ejudge and source: https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab
def get_pre_suc(root, key):
    pre, suc = Node(-1), Node(-1)
    while root:
        if root.key == key:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
            if root.right:
                suc = root.right
                while suc.left:
                    suc = suc.left
            return pre, suc

        if root.key > key:
            suc = root
            root = root.left
        else:
            pre = root
            root = root.right
    return pre, suc

class Solution:
   def findPreSuc(self, root, pre, suc, key):
        got_pre, got_suc = get_pre_suc(root, key)
        pre.key, suc.key = got_pre.key, got_suc.key