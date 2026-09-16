class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = ways to create j segments using first i points
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # prefix[i][j] = dp[1][j] + ... + dp[i][j]
        prefix = [[0] * (k + 1) for _ in range(n + 1)]

        # One way to choose 0 segments
        for i in range(n + 1):
            dp[i][0] = 1

        # Build prefix sums for j = 0
        for i in range(1, n + 1):
            prefix[i][0] = (prefix[i - 1][0] + dp[i][0]) % MOD

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                # Case 1: no segment ends at point i-1
                # Case 2: a segment ends at point i-1
                dp[i][j] = (
                    dp[i - 1][j] +
                    prefix[i - 1][j - 1]
                ) % MOD

                prefix[i][j] = (
                    prefix[i - 1][j] +
                    dp[i][j]
                ) % MOD

        return dp[n][k]