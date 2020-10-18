class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(TreeNode):
    """Encodes a tree to a single string.
    """
    serialization = ''

    # store as level order traversal (bfs)
    q = [root]
    
    # O(N)
    while q:
        curr = q.pop(0)

        # level order
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

        # serialize
        if q:
            serialization += (str(curr.val) + ',')
        else:
            serialization += str(curr.val)

    return serialization

def create_tree(curr, level, parent, data):
    if 2**level >= len(data):
        return

    curr.left = TreeNode(data[2*parent - 1])
    curr.right = TreeNode(data[2*parent])

    parent = data.index(curr.val)
    create_tree(curr.left, level+1, parent, data)
    parent = data.index(curr.val)
    create_tree(curr.right, level+1, parent, data)

def deserialize(data):
    """Decodes your encoded data to tree.
    """
    data = data.split(',')

    root = TreeNode(data[0])
    create_tree(root, 0, 1, data)

    return root


root = TreeNode(7)
root.left = TreeNode(12)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.right.left = TreeNode(9)
root.right.right = TreeNode(17)

print(serialize(root))

d_root = deserialize(serialize(root))

# bfs to see if correct
q = [d_root]
while q:
    curr = q.pop(0)
    print(curr.val)
    if curr.left:
        q.append(curr.left)
    if curr.right:
        q.append(curr.right)

print('\n')
print(d_root.val)
print(d_root.left.val)
print(d_root.right.val)
print(d_root.left.left.val)
print(d_root.left.right.val)
print(d_root.right.left.val)
print(d_root.right.right.val)