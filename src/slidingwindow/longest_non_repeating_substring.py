def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    size = len(s)
    arr = {c: -1 for c in range(26)}
    print(arr)
    window = 0
    i = 0
    max_win = 1
    while i < size:
        char_index = ord(s[i]) - ord('a')
        if arr[char_index] == -1:
            window = window + 1
        else:
            window = i - arr[char_index]

        if window > max_win:
            max_win = window

        arr[char_index] = i
        i = i + 1
    return max_win


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcdabcdef"))


def practice(s) -> int:
    size = len(s)
    # maps the character to the index in size. used to resize the window size.
    char_entry_map = {c: -1 for c in range(26)}  # 0 indexed

    i = 0
    window = 0
    ans = 1
    while i < size:
        char_index = ord(s[i]) - ord('a')

        if char_entry_map[char_index] != -1:  # not visited
            window = window + 1
        else:
            window = i - char_entry_map[char_index]

        char_entry_map[char_index] = i
        if window > ans:
            ans = window
        i = i + 1
    return ans
