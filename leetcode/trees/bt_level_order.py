def levelOrder(root):
    """Level order traversal is a breadth-first search (BFS)"""
    q = deque([root])
    traversal = []
    
    while q:
        # get node and add value to record of traversal
        curr = q.popleft()
        
        # TODO: how to know when done w/ a level? Leetcode submission wants format
        # based on list of lists, e.g. [[3],[9,20],[15,7]]
        
        traversal.append(curr.val)
        
        # add children to the queue
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        
    return traversal