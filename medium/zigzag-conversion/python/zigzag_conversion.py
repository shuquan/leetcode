class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        interval = 2 * numRows - 2
        zigzag = []
        j = 0
        k = 0
        if interval == 0:
            return s
        for i in xrange(numRows):
            j = i
            if i > 0 and i < numRows - 1:
                k = interval - i
                while j < length:
                    zigzag.append(s[j])
                    j = j + interval
                    if k < length:
                        zigzag.append(s[k])
                        k = k + interval
            else:
                while j < length:
                    zigzag.append(s[j])
                    j = j + interval
        return ''.join(zigzag)
