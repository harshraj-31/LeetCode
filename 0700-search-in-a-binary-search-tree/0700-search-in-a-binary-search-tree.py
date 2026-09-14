class Solution:
    def searchBST(self, root, val):
        current = root
        
        while current:
            # If we found the value, return the subtree
            if current.val == val:
                return current
            
            # If the target is smaller, search the left side
            elif val < current.val:
                current = current.left
                
            # If the target is larger, search the right side
            else:
                current = current.right
                
        # If we fall off the tree, the value doesn't exist
        return None