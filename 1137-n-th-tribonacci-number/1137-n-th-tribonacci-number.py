class Solution:
    def tribonacci(self, n: int) -> int:
        # Handle the base cases directly
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
            
        # These represent our starting window: T0, T1, and T2
        t0 = 0
        t1 = 1
        t2 = 1
        
        # Calculate from T3 up to Tn
        for _ in range(3, n + 1):
            # The new number is the sum of the previous three
            next_val = t0 + t1 + t2
            
            # Slide our window of three numbers forward
            t0 = t1
            t1 = t2
            t2 = next_val
            
        return t2