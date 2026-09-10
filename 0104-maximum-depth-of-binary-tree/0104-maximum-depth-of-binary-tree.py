class Solution:
    def maxDepth(self, root):
        # Base case: if the tree is empty, its depth is 0
        if not root:
            return 0
        
        # Find the depth of the left and right sides
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The max depth is the larger of the two sides, plus 1 for the current node
        return max(left_depth, right_depth) + 1