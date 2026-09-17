import heapq

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        
        for num in nums:
            # Push the current number into our heap
            heapq.heappush(min_heap, num)
            
            # If the heap grows larger than size k, remove the smallest number
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # The top of the min-heap will be exactly the kth largest element
        return min_heap[0]