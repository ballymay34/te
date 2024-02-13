# 23. Реализовать алгоритм пирамидальной сортировки.

import abc


class Heap(abc.ABC):
    @abc.abstractmethod
    def _higher(self, x, y):
        pass

    def __init__(self, arr=None):
        arr = [] if arr is None else arr
        self.heap = []
        for a in arr:
            self.push(a)

    def push(self, a):
        self.heap.append(a)
        self.__bottom_to_top(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise ValueError('heap is empty!')
        self.__swap(0, len(self.heap) - 1)
        max = self.heap.pop()
        self.__top_to_bottom(0)
        return max

    def __top_to_bottom(self, i):
        child = 2 * i + 1
        if child >= len(self.heap):
            return  # we are at a leaf
        if child + 1 < len(self.heap) and self._higher(self.heap[child + 1], self.heap[child]):
            child += 1  # choose right child because it should be higher
        if self._higher(self.heap[child], self.heap[i]):
            self.__swap(i, child)
            self.__top_to_bottom(child)

    def __bottom_to_top(self, i):
        parent = (i - 1) // 2
        if parent < 0:
            return  # we are at root
        if self._higher(self.heap[i], self.heap[parent]):
            self.__swap(i, parent)
            self.__bottom_to_top(parent)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class MinHeap(Heap):
    def _higher(self, a, b):
        return a < b


class MaxHeap(Heap):
    def _higher(self, a, b):
        return a >= b


def pyramid_sort(arr):
    h = MaxHeap(arr)
    res = []
    while h.heap:
        print(*h.heap)
        res.append(h.pop())
    return res


print(*pyramid_sort([5, 33, 6, 1, 42, 105, 68]))
print(*pyramid_sort([1, 2, 3, 4, 5, 6]))