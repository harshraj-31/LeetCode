class Solution:
    def deleteNode(self, root, key):
        # Base case: if the tree is empty or we don't find the key
        if not root:
            return None
            
        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: We found the node! Now, handle the 3 possible cases.
            
            # Case 1 & 2: The node has zero or one child.
            # If it only has a right child (or no children), return the right child.
            if not root.left:
                return root.right
            # If it only has a left child, return the left child.
            elif not root.right:
                return root.left
                
            # Case 3: The node has two children.
            # We need to find its "in-order successor" (the smallest value in its right subtree).
            current = root.right
            while current.left:
                current = current.left
                
            # Replace the current node's value with the successor's value.
            root.val = current.val
            
            # Delete the original successor node from the right subtree.
            root.right = self.deleteNode(root.right, root.val)
            
        return root