class Solution:
    def leafSimilar(self, root1, root2):
        # Helper function to collect leaves of a tree
        def get_leaves(node, leaves):
            if not node:
                return
            
            # If both children are missing, it's a leaf node!
            if not node.left and not node.right:
                leaves.append(node.val)
                
            # Traverse left, then right to maintain the left-to-right order
            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)

        leaves1 = []
        leaves2 = []
        
        # Populate the leaf lists for both trees
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)
        
        # Check if the sequences are identical
        return leaves1 == leaves2