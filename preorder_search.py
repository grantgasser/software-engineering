class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        isInTree = False
        isInTree = self.preorder_search(self.root, find_val)
        
        return isInTree

    def preorder_search(self, start, find_val):
            """Helper method - use this to create a 
            recursive search solution."""
            if start.value == find_val:
                return True
                
            else:
                if start.left:
                    self.preorder_search(start.left, find_val)
                elif start.right:
                    self.preorder_search(start.right, find_val)