class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            length = right - left

            if length > max_length:
                max_length = length

        return max_length