class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base cases for n = 1, 2, 3
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
            
        # dp1 represents dp[i-3]
        # dp2 represents dp[i-2]
        # dp3 represents dp[i-1]
        dp1, dp2, dp3 = 1, 2, 5
        
        for _ in range(4, n + 1):
            # Formula: dp[i] = 2 * dp[i-1] + dp[i-3]
            current = (2 * dp3 + dp1) % MOD
            
            # Slide the window forward
            dp1 = dp2
            dp2 = dp3
            dp3 = current
            
        return dp3