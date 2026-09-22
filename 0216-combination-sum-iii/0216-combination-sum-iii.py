class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        
        def backtrack(start_number, current_combination, current_sum):
            # Base Case 1: We found exactly 'k' numbers
            if len(current_combination) == k:
                # If they add up to 'n', we found a winning combination!
                if current_sum == n:
                    # We must append a COPY of the list, not the original reference
                    result.append(list(current_combination))
                return
            
            # Pruning (Optimization): If our sum is already too big, stop searching
            if current_sum > n:
                return
                
            # Try every number from our starting point up to 9
            for i in range(start_number, 10):
                # Choose the number
                current_combination.append(i)
                
                # Explore further (passing i + 1 because we can't reuse numbers)
                backtrack(i + 1, current_combination, current_sum + i)
                
                # Backtrack: undo the choice so we can try the next number
                current_combination.pop()
                
        # Start the search at number 1, with an empty list and a sum of 0
        backtrack(1, [], 0)
        
        return result