class Solution:
    def pivotInteger(self, n):
        total = n * (n + 1) // 2

        left_sum = 0

        for x in range(1, n + 1):
            left_sum += x

            if left_sum == total - left_sum + x:
                return x

        return -1