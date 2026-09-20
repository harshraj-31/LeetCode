class Solution:
    def successfulPairs(self, spells, potions, success):
        # Sort the potions from weakest to strongest
        potions.sort()
        
        result = []
        m = len(potions)
        
        for spell in spells:
            left = 0
            right = m - 1
            
            # Default to m in case no potion is strong enough
            first_success_idx = m 
            
            # Binary search to find the weakest potion that makes a successful pair
            while left <= right:
                mid = (left + right) // 2
                
                if spell * potions[mid] >= success:
                    # This potion works! Save its index.
                    first_success_idx = mid
                    
                    # Check the left side to see if an even weaker potion also works
                    right = mid - 1
                else:
                    # This potion is too weak, search the right side for a stronger one
                    left = mid + 1
                    
            # If the first valid potion is at 'first_success_idx', 
            # then all potions from there to the end of the list are also valid!
            result.append(m - first_success_idx)
            
        return result