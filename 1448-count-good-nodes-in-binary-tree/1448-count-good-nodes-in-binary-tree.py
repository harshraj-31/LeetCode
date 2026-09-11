class Solution:
    def goodNodes(self, root):
        
        def dfs(node, max_so_far):
            # Base case: if we reach an empty space, there are 0 good nodes
            if not node:
                return 0
            
            count = 0
            # If the current node is at least as big as the max seen so far, it's a good node!
            if node.val >= max_so_far:
                count = 1
            
            # Update the highest value seen on this path
            new_max = max(max_so_far, node.val)
            
            # Check the left and right children, passing down the new max
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count

        # Start the search at the root, using the root's own value as the initial max
        return dfs(root, root.val)