class Solution(object):   
    def permute(self, nums):
        print("start", nums)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if (len(nums) == 1):
            print("end", nums)
            return [nums[:]]
        
        for i in range(len(nums)):
            print("popped", nums, nums[0])
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
                print("perm", n, perm)
            result.extend(perms)
            nums.append(n)
            print("after", n, nums)
            
        print("end", nums)
        return result
