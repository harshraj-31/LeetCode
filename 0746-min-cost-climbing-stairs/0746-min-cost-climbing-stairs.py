class Solution:
    def minCostClimbingStairs(self, cost):
        # We start by paying the toll for the first two possible starting steps
        first = cost[0]
        second = cost[1]
        
        # Calculate the minimum cost to land on every subsequent step
        for i in range(2, len(cost)):
            # The cost to stand on the CURRENT step is its own toll plus 
            # the cheaper of the two paths we could have taken to get here.
            current = cost[i] + min(first, second)
            
            # Slide our window of two steps forward
            first = second
            second = current
            
        # To clear the final staircase (reach the top), we can either step off 
        # from the very last step, or skip it by jumping from the second-to-last step.
        return min(first, second)