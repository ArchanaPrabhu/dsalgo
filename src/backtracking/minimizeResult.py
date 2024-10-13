class Solution(object):
    def minimizeResult(self, exp):
        """
        :type expression: str
        :rtype: str
        """
        # since we know that we have + sign, traverse till you find +
        # move left and right pointer till we reach mininum value
        # we store the state of min value and then save it
        # can we use the 
        # 247 + 38
        def getInt(v):
            if (v == ""):
                return 1
            return int(v)

        str_arr = exp.split("+")
        min_v = float("infinity")
        left, right = str_arr[0], str_arr[1]
        print(left, right)
        len_l, len_r = len(str_arr[0]), len(str_arr[1])
        len_i = min(len_l, len_r)
        for i in range(len_l - 1, -1, -1):
            for j in range(0, len_r):
                print("print", (left[:i] + "(" + left[i:] + "+" + right[:j + 1] + ")" + right[j+1:]))
                value = getInt(left[:i]) * ( int(left[i:]) + int(right[:j + 1])) * getInt(right[j+1:])
                if (value < min_v):
                    min_v = value
                    ans = (left[:i] + "(" + left[i:] + "+" + right[:j + 1] + ")" + right[j+1:])
        
        return ans

       
