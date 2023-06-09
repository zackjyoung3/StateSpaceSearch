import random
import unittest
import heapq

from priority_queue import MinPriorityQueue


class MinPriorityQueueTestClass(unittest.TestCase):
    def setUp(self):
        self.obj = MinPriorityQueue()

    def tearDown(self):
        pass

    def test_1_100_ascending_insert(self):
        for i in range(1, 101):
            self.obj.enqueue(i)
            self.assertEqual(self.obj.heap_min(), 1)

        for i in range(1, 101):
            self.assertEqual(self.obj.heap_min(), i)
            self.assertEqual(self.obj.dequeue(), i)

        self.test_raises_correctly()

    def test_100_1_descending_insert(self):
        for i in range(100, 0, -1):
            self.obj.enqueue(i)
            self.assertEqual(self.obj.heap_min(), i)

        for i in range(1, 101):
            self.assertEqual(self.obj.heap_min(), i)
            temp = self.obj.dequeue()
            self.assertEqual(temp, i)

        self.test_raises_correctly()

    def test_random_inserts(self):
        queue = []
        for _ in range(10000):
            rand_int = random.randint(1, 1_000_000)
            heapq.heappush(queue, rand_int)
            self.obj.enqueue(rand_int)
            self.assertEqual(self.obj.heap_min(), queue[0])

        for _ in range(10000):
            self.assertEqual(self.obj.heap_min(), queue[0])
            self.assertEqual(self.obj.dequeue(), heapq.heappop(queue))

    def test_more_random_inserts(self):
        queue = []
        for _ in range(1_000_000):
            rand_int = random.randint(1, 1_000_000_000)
            heapq.heappush(queue, rand_int)
            self.obj.enqueue(rand_int)
            self.assertEqual(self.obj.heap_min(), queue[0])

        for _ in range(1_000_000):
            self.assertEqual(self.obj.heap_min(), queue[0])
            self.assertEqual(self.obj.dequeue(), heapq.heappop(queue))

    def test_raises_correctly(self):
        with self.assertRaises(IndexError):
            self.obj.heap_min()

        with self.assertRaises(IndexError):
            self.obj.dequeue()


if __name__ == '__main__':
    unittest.main()