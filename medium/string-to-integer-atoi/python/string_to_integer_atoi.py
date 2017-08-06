class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        result = 0
        i = 0
        s = 1
        if len(str) > 0 and str[0] == '-':
            str = str[1:]
            s = -1
        elif len(str) > 0 and str[0] == '+':
            str = str[1:]
            s = 1

        if len(str) > 0 and not str[0].isdigit():
            return 0

        for e in reversed(str):
            if not e.isdigit():
                result = 0
                i = -1
            else:
                result = result + int(e) * (10 ** i)
            i = i + 1

        result = s * result
        if result > 0x7fffffff:
            return 0x7fffffff
        elif result < -0x80000000:
            return -0x80000000
        else:
            return result
