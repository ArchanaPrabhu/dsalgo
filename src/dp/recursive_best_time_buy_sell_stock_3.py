class Solution(object):
    def maxProfitRecursive(self, index, prices, count, profit_arr):
        if (count == 2):
            return 0
        if (profit_arr[index] != -1):
            return profit_arr[index]
        max_profit = -1
        for i in range(index, len(prices)):
            price = prices[i]
            for j in range(i+1, len(prices)):
                possible_profit = (prices[j] - price)
                max_profit = max(max_profit, possible_profit + self.maxProfitRecursive(j, prices, 1 + count, profit_arr))
                # print("max_profit", prices[i], prices[j], max_profit)
        
        profit_arr[index] = max_profit
        if (max_profit == -1): return 0
        else: return max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit_arr = [-1 for _ in range(len(prices))]
        return self.maxProfitRecursive(0, prices, 0, profit_arr)
        


