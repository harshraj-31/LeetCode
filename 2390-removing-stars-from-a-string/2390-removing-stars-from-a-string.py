class Solution:
    def removeStars(self, s):
        result = []

        for char in s:
            if char == "*":
                result.pop()
            else:
                result.append(char)

        return "".join(result)