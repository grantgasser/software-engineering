"""
Heapq: Heap data structure in Python

Heap review: https://www.youtube.com/watch?v=HqPJF2L5h9U

Python heapq docs: https://docs.python.org/3/library/heapq.html#module-heapq

CTCI: https://www.youtube.com/watch?v=t0Cq6tVNRBA
    => best to use an array to represent heap
"""
import heapq

# NOTE: default is min heap

# heapify an existing arr/binary tree
arr = [5, 7, 9, 1, 3]
heapq.heapify(arr)  # modifies in place, doesn't return value
print(arr)

# Insert: always goes in bottommost, leftmost spot
# push value to heap
heapq.heappush(arr, 4)
print(arr)

# remove and return min (or max if maxheap)
heapq.heappop(arr)
print(arr)

