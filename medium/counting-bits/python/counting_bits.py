class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num+1):
            result.append(bin(i).count('1'))
        return result
