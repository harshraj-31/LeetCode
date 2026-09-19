class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            # Call the pre-defined API
            result = guess(mid)
            
            if result == 0:
                # We found the exact number!
                return mid
            elif result == -1:
                # Our guess was too high, so the target must be smaller.
                # Shift our search to the left half.
                right = mid - 1
            else:
                # Our guess was too low, so the target must be bigger.
                # Shift our search to the right half.
                left = mid + 1