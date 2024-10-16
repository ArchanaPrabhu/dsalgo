class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l + r) // 2

            if (nums[mid] == target):
                return mid

            if (nums[l] <= nums[mid]):
            # if left part is sorted, check if it could not belong to the left
                if (target < nums[l] or target > nums[mid]):
                    # move to the right
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if (target < nums[mid] or target > nums[r]):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
