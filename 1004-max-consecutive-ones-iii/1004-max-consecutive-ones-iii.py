class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Too many zeros, move left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length