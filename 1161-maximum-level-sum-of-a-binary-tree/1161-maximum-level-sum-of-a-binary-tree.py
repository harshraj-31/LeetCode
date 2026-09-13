from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])
        current_level = 1
        
        max_sum = float('-inf')
        max_level = 1
        
        while queue:
            level_length = len(queue)
            level_sum = 0
            
            # Process all nodes in the current level
            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # If we found a strictly greater sum, update our max tracker
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
                
            current_level += 1
            
        return max_level