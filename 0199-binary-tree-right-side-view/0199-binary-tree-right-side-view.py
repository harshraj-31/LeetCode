from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            # Number of nodes at the current level
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # If this is the last node in the current level, we can see it!
                if i == level_length - 1:
                    result.append(node.val)
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result