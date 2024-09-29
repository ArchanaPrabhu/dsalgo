class Solution(object):
    def isPalindrome(self, s):
        # print(s, str(reversed(s)), s == reversed(s))
        return s == s[::-1]

    # abc
    def countSubstrings(self, s):
        ans = 0
        for w in range(1, len(s) + 1, 1):
            for i in range(len(s)):
                # print(str(s[i]), w, i + w)
                if (i + w <= len(s)):
                    # print(s[i:i+w])
                    if (self.isPalindrome(s[i:i+w])):
                        ans += 1
        return ans        
