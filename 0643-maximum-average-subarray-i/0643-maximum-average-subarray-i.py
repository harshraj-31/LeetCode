class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)

        current_sum = 0

        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum

        for i in range(k, n):
            current_sum = current_sum - nums[i - k] + nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k