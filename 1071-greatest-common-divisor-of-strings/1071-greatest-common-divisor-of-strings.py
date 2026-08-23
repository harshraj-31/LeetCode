class Solution:
    def gcdOfStrings(self, str1, str2):
        # If they don't have the same repeating pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD of the lengths
        a = len(str1)
        b = len(str2)

        while b != 0:
            a, b = b, a % b

        return str1[:a]