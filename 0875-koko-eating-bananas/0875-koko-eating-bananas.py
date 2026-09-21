import math

class Solution:
    def minEatingSpeed(self, piles, h):
        # Koko can eat at least 1 banana per hour
        left = 1
        # The fastest she ever needs to eat is the size of the biggest pile
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate how many hours it takes to eat everything at 'mid' speed
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / mid)
                
            # If she finishes within the time limit 'h'
            if hours_spent <= h:
                # She successfully finished! But maybe she can go even slower?
                # We search the left half to see if a smaller speed works.
                right = mid
            else:
                # She was too slow and ran out of time. 
                # She MUST eat faster, so we search the right half.
                left = mid + 1
                
        return left