class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        count1 = {}
        count2 = {}

        for char in word1:
            count1[char] = count1.get(char, 0) + 1

        for char in word2:
            count2[char] = count2.get(char, 0) + 1

        # Both strings must contain the same characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # The frequencies must be the same, but their order doesn't matter
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True