class Solution:
    def decodeString(self, s):
        stack = []
        number = 0
        current = ""

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)

            elif char == "[":
                stack.append((current, number))
                current = ""
                number = 0

            elif char == "]":
                previous, repeat = stack.pop()
                current = previous + current * repeat

            else:
                current += char

        return current