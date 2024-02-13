# 19. Даны два упорядоченных по невозрастанию односвязных списка.
# Объедините их в новый упорядоченный по невозрастанию односвязный список.

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def __str__(self):
        return f'{self.val} {self.next}'

def merge_sorted(n1, n2):
    first = Node(None, None)
    last = first
    while n1 or n2:
        new_val = None
        if n1 and n2 and n1.val >= n2.val or n1 and not n2:
            new_val = n1.val
            n1 = n1.next
        else:
            new_val = n2.val
            n2 = n2.next
        last.next = Node(new_val, None)
        last = last.next
    return first.next

n1 = Node(12, Node(9, Node(7, Node(5, None))))
print(n1)
n2 = Node(15, Node(8, Node(6, Node(4, None))))
print(n2)

print(merge_sorted(n1, n2)) 