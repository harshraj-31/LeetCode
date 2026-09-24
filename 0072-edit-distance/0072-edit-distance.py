class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        n = len(word2)
        prev = list(range(n + 1))

        for i in range(1, len(word1) + 1):
            curr = [i] + [0] * n
            char = word1[i - 1]

            for j in range(1, n + 1):
                if char == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    best = prev[j - 1]

                    if prev[j] < best:
                        best = prev[j]

                    if curr[j - 1] < best:
                        best = curr[j - 1]

                    curr[j] = best + 1

            prev = curr

        return prev[n]