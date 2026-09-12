class Solution:
    def longestZigZag(self, root):
        self.max_length = 0
        
        # Helper function to explore the tree
        def dfs(node, direction, length):
            if not node:
                return
            
            # Update the longest zigzag seen so far
            if length > self.max_length:
                self.max_length = length
            
            if direction == "left":
                # We just came from a left move.
                # To continue the zigzag, we MUST go right.
                dfs(node.right, "right", length + 1)
                
                # If we go left again, we break the pattern. 
                # A brand new zigzag starts here with a length of 1.
                dfs(node.left, "left", 1)
                
            elif direction == "right":
                # We just came from a right move.
                # To continue the zigzag, we MUST go left.
                dfs(node.left, "left", length + 1)
                
                # If we go right again, we break the pattern.
                # A brand new zigzag starts here with a length of 1.
                dfs(node.right, "right", 1)

        # Start from the root by trying both possible initial directions.
        # Moving to a child counts as the first edge (length 1).
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)
        
        return self.max_length