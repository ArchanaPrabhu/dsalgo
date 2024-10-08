# Input : arr[] = {3, 6, 12, 1, 5, 8}
# Output : 6 3 12 1 8 5 

# Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
# Output : 10 9 18 7 20 19 4 13 14 21 

def solution(nums):
    if (len(nums) == 0 or len(nums) == 1):
        return nums

    even_pointer = 0
    even_needs_swapping = False
    odd_pointer = 1
    odd_needs_swapping = False
    while even_pointer < len(nums) and odd_pointer < len(nums):
        if (nums[even_pointer]%2 != 0):
            even_needs_swapping = True
        else:
            even_pointer += 2
        
        if (nums[odd_pointer]%2 != 1):
            odd_needs_swapping = True
        else:
            odd_pointer += 2
        
        if (even_needs_swapping and odd_needs_swapping):
            temp = nums[even_pointer]
            nums[even_pointer] = nums[odd_pointer]
            nums[odd_pointer] = temp
            even_pointer += 2
            odd_pointer += 2
    
    return nums

print(solution([3, 6, 12, 11, 5, 8]))
