|  Problem | Approach  |  things to remember |
| - | - | - |
| Longest Palindromic Substring  | for every index check the odd and even length palindrom. o(n2)  |   |
| Maximum Subarray  | calculate prefixes, if prefixSum < 0, reset it. Find max of the values outstanding. Simple |   |
| Maximum product subarray| since they can have -ve numbers, keep a track of the min product and max product, calculate which is more based on the current index value. Simple | |
| Longest Substring Without Repeating Characters  |  use a char Set, sliding window, simple code, use l and r. l = 0, while r is in the range of the string. for every string, keep a count. then use a whil loop to increment l till window - max_occuring_value == k, record the max window length|   |
| Longest increasing subsequence  | for every element check for a possibility when you find something greater than that current number. This can be improved by using 2 for loop, <br />for i in range(n-1), -1, -1 <br /> for j in range(i+1, len(nums) <br />if (num[i] < num[j] <br />lis[i] = max(lis[i], 1+lis[j]) | DP |
| Longest common subsequence | this is for 2 strings, use 2D dp to do matching | |
| Longest consecutive subsequence | create a set of the array, check if it's previous number is present, if it is beginning of a sequence, start searching for sequence and keep a max of it| simple |
| Longest repeating character replacement| tricky but simple code. Logic is to keep the count| |
| minimum window substring | | |
| subset sum equal to K | use target and index approach, start from n and move till 0. <br />if target == 0 return true  <br />if index == 0 return false  <br />return taken and notTaken | DP |

|  Problem | Approach  |  things to remember |
| - | - | - |
|House Robber 2 |  | |
| Number of islands| | |
| rotate image | | |
| word search | | |
| kth smallest element in a bst| | | 
| search in rotated sorted array| | |
| min in rotated sorted array| | |




