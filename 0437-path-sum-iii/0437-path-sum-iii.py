class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        
        # Helper function: Counts valid paths starting from EXACTLY this node
        def count_paths(node, current_target):
            if not node:
                return 0
            
            paths = 0
            # If we hit the exact target, we found a valid path
            if node.val == current_target:
                paths += 1
            
            # Keep looking downwards (because node values can be negative, 
            # a path could hit the target, go off, and hit it again)
            paths += count_paths(node.left, current_target - node.val)
            paths += count_paths(node.right, current_target - node.val)
            
            return paths

        # Total paths = 
        # 1. Paths starting from the current root
        # 2. Paths starting somewhere in the left subtree
        # 3. Paths starting somewhere in the right subtree
        return (count_paths(root, targetSum) + 
                self.pathSum(root.left, targetSum) + 
                self.pathSum(root.right, targetSum))