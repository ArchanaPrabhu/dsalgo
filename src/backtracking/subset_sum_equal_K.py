from os import *
from sys import *
from collections import *
from math import *

# this method makes sure that a subset sums upto K - any combination works
def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[-1 for _ in range(k+1)] for _ in range(n)]
    
    # if the array[]
    return recurse(n - 1, k, arr, dp)
    # 4 3 2 1 


def recurse(index, target, arr, dp):
    # print("recurse start", arr[index], target)
    if (target == 0):
        return True
    
    if (index == 0):
        # print("return", arr[index], target == arr[index])
        return target == arr[index]
        
    if (arr[index] == target):
        return True
    
    if(dp[index][target] != -1):
        # print("dp", index, target)
        return dp[index][target]
    
    # print("recurse exclude", arr[index], target)
    notTaken = recurse(index - 1, target, arr, dp)
    taken = False
    if (target - arr[index] > 0):
        # print("recurse include", arr[index], target)
        taken = recurse(index - 1, target - arr[index], arr, dp)
    # print("recurse end", arr[index], target, taken or notTaken)
    dp[index][target] = taken or notTaken
    return taken or notTaken

    

