print("Hello World!")

def convert_list_tuple(l):
    return tuple(l)

def group_anagrams(str_arr):
    if (len(str_arr) <= 1):
        return [ str_arr ]
    
    ans = {}
    
    for i in range(len(str_arr)):
        char_repr = [0 for _ in range(26)] # reset to 0, 1,...25   
        for c in str_arr[i]:
            char_repr[ord(c) - ord("a")] += 1
        if convert_list_tuple(char_repr) in ans:
            ans[convert_list_tuple(char_repr)].append(str_arr[i])
        else:
            ans[convert_list_tuple(char_repr)] = [str_arr[i]]
    return ans
    

if __name__ == "__main__":
    print(convert_list_tuple([1, 2, 3]))
    print(list(group_anagrams(["eat","tea","tan","ate","nat","bat"]).values()))
