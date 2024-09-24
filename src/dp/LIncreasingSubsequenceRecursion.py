class Solution(object):
    def findLISForRange(self, index, nums, dp):
        if (index == len(nums) - 1):
            dp[index] = 0
            print("return", nums[index], dp[index])
            return 0
        
        if (dp[index] != -1):
            return dp[index]

        for j in range(index + 1, len(nums)):
            if nums[j] > nums[index]:
                # print("explore", nums[index], nums[j])            
                dp[index] = max(dp[index], 1 + self.findLISForRange(j, nums, dp))
                # print("populate", nums[index], nums[j], dp[index])
        if (dp[index] == -1):
            return 0
        return dp[index]

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 10  9 2   5   3  7  101 18
        #                      0   0
        dp = [ -1 for _ in range(len(nums))]
        ans = -1
        for i in range(len(nums)):
            ans = max(ans, self.findLISForRange(i, nums, dp))
            print("ans", nums[i], i, ans)
        return ans + 1
        
    # [10,9,2,5,3,7,101,18]
    #           3 2  1   1
    
