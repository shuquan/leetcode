class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sign = cmp(x, 0)
        if sign < 0:
            return False
        y = sign * int(str(sign * x)[::-1])
        if cmp(x, y) == 0:
            return True
        else:
            return False
