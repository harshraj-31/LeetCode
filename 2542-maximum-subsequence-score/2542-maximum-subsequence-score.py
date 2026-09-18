import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        # Step 1: Pair the numbers up and sort them descending based on nums2
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        # Step 2: Iterate through the sorted pairs
        for num1, num2 in pairs:
            # Add the current nums1 to our heap and running sum
            heapq.heappush(min_heap, num1)
            current_sum += num1
            
            # If we have more than k elements, kick out the smallest nums1
            if len(min_heap) > k:
                smallest_num1 = heapq.heappop(min_heap)
                current_sum -= smallest_num1
                
            # Step 3: Once we have exactly k elements, calculate the score
            if len(min_heap) == k:
                # Because we sorted by nums2 descending, the current num2 
                # is guaranteed to be the minimum of our selected group!
                max_score = max(max_score, current_sum * num2)
                
        return max_score