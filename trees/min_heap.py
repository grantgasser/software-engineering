"""
pg. 116 CTCI

Min Heap: Complete binary tree where each node is smaller than its children. Therefore, 
the root is the minimum element in the tree.

2 main operations: insert() and extract_min()

Start insert at the bottom right and swap new element with its parent if elem < parent (bubble/percolate)
    - O(log n)

Finding min is O(1), removing min is O(log n). To remove min, 
"""
