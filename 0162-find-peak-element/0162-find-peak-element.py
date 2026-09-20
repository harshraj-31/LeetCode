class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the number to our right is bigger, we are walking uphill.
            # Therefore, a peak MUST exist to our right.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
                
            # If the number to our right is smaller, we are walking downhill.
            # Therefore, the peak is either exactly where we are, or to our left.
            else:
                right = mid
                
        # When left and right converge, they point to a peak.
        return left