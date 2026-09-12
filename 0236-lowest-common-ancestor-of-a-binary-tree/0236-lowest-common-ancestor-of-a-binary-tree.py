class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base case: if we reach an empty node, or if we find either p or q
        if not root or root == p or root == q:
            return root
        
        # Search for p and q in the left and right branches
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If we found something in BOTH the left and right branches, 
        # it means p and q are on opposite sides of the current node. 
        # Therefore, the current node is their lowest common ancestor!
        if left and right:
            return root
            
        # Otherwise, if we only found something in one branch, 
        # pass that found node back up the chain.
        return left if left else right