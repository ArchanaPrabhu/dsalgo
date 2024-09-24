class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:    
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1): # 1 2 3 4 . . . 
            for j in range(len(coins)):
                if (i - coins[j] >= 0):
                    print(i, coins[j], dp[i])
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        if (dp[amount] == (amount + 1)):
            return -1
        return dp[amount]


        
