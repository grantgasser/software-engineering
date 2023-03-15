def lowest_common_ancestor(root, p, q):
    # If both elements are less than the root, move to the left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both elements are greater than the root, move to the right subtree
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # If one element is less than and the other is greater than the root, or if one element matches the root, then the root is the LCA
    else:
        return root