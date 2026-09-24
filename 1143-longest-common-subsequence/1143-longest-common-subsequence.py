class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        masks = {}
        for i, ch in enumerate(text1):
            masks[ch] = masks.get(ch, 0) | (1 << i)

        row = 0
        for ch in text2:
            x = row | masks.get(ch, 0)
            row = x & ((x - ((row << 1) | 1)) ^ x)

        return bin(row).count("1")