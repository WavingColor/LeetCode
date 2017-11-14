# Given two binary strings, return their sum (also a binary string).

# Have you met this question in a real interview? Yes
# Example
# a = 11

# b = 1

# Return 100

class Solution:
    """
    @param: a: a number
    @param: b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        la = len(a)
        lb = len(b)
        maxl = max(la, lb)
        
        res = ''
        upnum = 0
        for i in range(maxl):
            # print(la, lb, i)
            ta = 0
            tb = 0
            if la > i:
                ta = int(a[la-i-1])
            if lb > i:
                tb = int(b[lb-i-1])
            tr = ta + tb + upnum
            # print(tb, ta, tr,i, la, lb)
            if tr > 1:
                upnum = 1
                tr = tr%2
            else:
                upnum = 0
            res = str(tr) + res
        if upnum == 1:
            res = str(upnum) + res
        return res
            

a = '111'
b = '1001'
print(Solution().addBinary(a, b))