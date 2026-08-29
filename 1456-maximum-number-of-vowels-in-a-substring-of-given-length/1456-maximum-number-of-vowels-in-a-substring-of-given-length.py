class Solution:
    def maxVowels(self, s, k):
        vowels = "aeiou"

        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            if count > max_count:
                max_count = count

        return max_count