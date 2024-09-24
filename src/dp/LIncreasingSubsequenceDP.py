class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 10  9 2   5   3  7  101 18
        dp = [ 1 for _ in range(len(nums))]
        ans = -1

        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                dp[i] = 1
            
            for j in range(i + 1, len(nums)):
                if (nums[j] > nums[i]):
                    dp[i] = max(dp[i], 1 + dp[j])
        ans = -1
        for i in range(len(dp)):
            ans = max(ans, dp[i])

        return ans

        
    
