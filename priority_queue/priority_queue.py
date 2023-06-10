import math


def parent(i: int) -> int:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


class MinPriorityQueue:
    def __init__(self):
        self.heap = [None for _ in range(10)]
        self.heap_size = 0

    def is_empty(self):
        return self.heap_size == 0

    def heap_min(self):
        if self.is_empty():
            raise IndexError('There are no elements in the heap')
        return self.heap[0]

    def dequeue(self):
        if self.is_empty():
            raise IndexError('There are no elements in the heap: heap underflow')
        min_element = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.min_heapify(0)

        if self.heap_size <= len(self.heap) // 2 and len(self.heap) > 10:
            new_size = max((len(self.heap) // 3) * 2, 10)
            self.heap = self.heap[:new_size]

        return min_element

    def min_heapify(self, i: int):
        left_child = left(i)
        right_child = right(i)
        smallest = i

        if left_child < self.heap_size and self.heap[left_child] < self.heap[i]:
            smallest = left_child

        if right_child < self.heap_size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def enqueue(self, key):
        self.heap_size += 1
        if self.heap_size == len(self.heap):
            for _ in range(self.heap_size):
                self.heap.extend([None] * self.heap_size)
        self.heap[self.heap_size - 1] = math.inf
        self.heap_decrease_key(self.heap_size - 1, key)

    def heap_decrease_key(self, i, key):
        if key > self.heap[i]:
            raise Exception('New key is larger than current key')
        self.heap[i] = key
        while i > 0 and self.heap[parent(i)] > self.heap[i]:
            self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
            i = parent(i)
