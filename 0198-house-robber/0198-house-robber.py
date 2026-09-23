class Solution:
    def rob(self, nums):
        # rob1 tracks the max money up to 2 houses ago
        # rob2 tracks the max money up to 1 house ago
        rob1, rob2 = 0, 0
        
        for n in nums:
            # The max money at the current house is the better of:
            # 1. Robbing the current house (n) + max money from 2 houses ago (rob1)
            # 2. Skipping the current house and keeping max money from 1 house ago (rob2)
            temp = max(n + rob1, rob2)
            
            # Slide our window of two houses forward
            rob1 = rob2
            rob2 = temp
            
        return rob2