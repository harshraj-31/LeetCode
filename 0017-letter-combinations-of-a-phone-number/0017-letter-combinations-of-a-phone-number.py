class Solution:
    def letterCombinations(self, digits):
        # Edge case: If the input is empty, return an empty list immediately
        if not digits:
            return []
            
        # Map out the telephone buttons to their corresponding letters
        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        
        result = []
        
        # Helper function to build the combinations
        def backtrack(index, current_string):
            # Base case: If our string is the same length as the input digits,
            # we have a complete combination!
            if index == len(digits):
                result.append(current_string)
                return
                
            # Find which digit we are currently looking at
            current_digit = digits[index]
            
            # Loop through all the letters that this digit represents
            for letter in phone_map[current_digit]:
                # Recursively call the function for the next digit, 
                # adding the current letter to our ongoing string
                backtrack(index + 1, current_string + letter)
                
        # Start the backtracking process at index 0 with an empty string
        backtrack(0, "")
        
        return result