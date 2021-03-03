"""
Heap Implementation: better to use array than Heap class with Node class!

Main methods are insert and get_min

Some help: https://www.youtube.com/watch?v=t0Cq6tVNRBA

Note: can also use heapq module. See general_python/heapq.
"""
class minHeap(object):
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        """Swap elements in heap array"""
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def get_min(self):
        """Return max value of heap"""
        return self.heap[0]

    def extract_min(self):
        """Return and delete min. Replace min w/ bottom left and bubble down/heapify down"""
        pass

    def get_parent_idx(self, idx):
        """Get parent_idx of idx"""
        return (idx - 1) // 2

    def has_larger_parent(self, idx):
        """Return parent_idx if this idx has a parent and the parent is larger, F otherwise"""
        parent_idx = self.get_parent_idx(idx)
        if parent_idx >= 0 and self.heap[parent_idx] > self.heap[idx]:
            return True
        else:
            return False

    def insert(self, x):
        """Insert at bottom right and bubble up"""
        self.heap.append(x)  # very easy to add to bottom right

        # bubble up (heapify up)
        idx = len(self.heap) - 1
        while self.has_larger_parent(idx):
            parent_idx = self.get_parent_idx(idx)
            self.swap(parent_idx, idx)
            idx = parent_idx


import heapq

nums = [3, 2, 1, 5, 6, 4]
heapq.heapify(nums)
print(nums)

h = minHeap()
h.insert(3)
h.insert(2)
h.insert(1)
h.insert(5)
h.insert(6)
h.insert(4)
print(h.heap)  # different, but still valid min heap