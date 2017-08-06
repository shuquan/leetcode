class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        if x < 0:
            result = -int(s[-1:0:-1])
            if result < -0x7fffffff:
                return 0
            else:
                return result
        else:
            result = int(s[::-1])
            if result > 0x7fffffff:
                return 0
            else:
                return result
