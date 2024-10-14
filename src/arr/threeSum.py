class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        # print(nums)
        ans = []
        for index, value in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            target = 0 - value
            
            while (left < right):
                cur_sum = nums[left] + nums[right]
                # print(nums[left:right+1], target, value, cur_sum)
                if (cur_sum == target):
                    if ((value, nums[left], nums[right]) not in ans):
                        ans.append((value, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif (cur_sum > target):
                    right -= 1
                else:
                    left += 1
        return ans
            
