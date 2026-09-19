import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        left_heap = []
        right_heap = []
        
        # Pointers to keep track of the next available workers in the middle
        left = 0
        right = len(costs) - 1
        
        # Fill the initial left heap with the first 'candidates' workers
        while left < candidates and left <= right:
            heapq.heappush(left_heap, costs[left])
            left += 1
            
        # Fill the initial right heap with the last 'candidates' workers
        # The 'left <= right' ensures we don't accidentally add the same worker twice 
        # if the candidate pools overlap.
        while right >= len(costs) - candidates and left <= right:
            heapq.heappush(right_heap, costs[right])
            right -= 1
            
        total_cost = 0
        
        # Hire exactly k workers
        for _ in range(k):
            # We pick from the left heap if:
            # 1. The right heap is empty, OR
            # 2. Left heap has a smaller or equal cost (equal favors left due to smaller index rule)
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total_cost += heapq.heappop(left_heap)
                
                # Replace the hired worker with the next available worker from the left
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(right_heap)
                
                # Replace the hired worker with the next available worker from the right
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1
                    
        return total_cost