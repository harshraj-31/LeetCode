class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maximum = max(candies)

        for candy in candies:
            if candy + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)

        return result