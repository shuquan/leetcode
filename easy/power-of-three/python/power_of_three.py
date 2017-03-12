class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 2 or n < 1:
            return False
        elif n == 3 or n == 1:
            return True
        elif n > 3 and n % 3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False

    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == 1 or n % 3 ==0 and self.isPowerOfThree(n/3)
