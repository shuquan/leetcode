class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = [([False]*len(s)) for i in xrange(len(s))]
        i = 0
        length = 1
        substring = ''
        while length <= len(s):
            for i in xrange(len(s)):
                if length == 1:
                    table[i][i] = True
                    substring = s[i:i+1]
                if length == 2 and i + 1 < len(s) and s[i] == s[i+1]:
                    table[i][i+1] = True
                    substring = s[i:i+2]
                elif length > 2 and length + i - 1 < len(s):
                    table[i][length+i-1] = table[i+1][length+i-2] and (s[i] == s[length+i-1])
                    if table[i][length+i-1] and length >= len(substring):
                        substring = s[i:length+i]

            length = length + 1

        return substring

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str

	optimized runtime by setting len(s) to a variable and seperate the for statement.

        """
        n = len(s)
        table = [([False]*n) for i in xrange(n)]
        i = 0
        length = 1
        substring = ''
        while length <= n:
            if length == 1:
                for i in xrange(n):
                    table[i][i] = True
                    substring = s[i:i+1]
            if length == 2:
                for i in xrange(n - 1):
                    if s[i] == s[i+1]:
                        table[i][i+1] = True
                        substring = s[i:i+2]
            elif length > 2:
                for i in xrange(n - length + 1):
                    table[i][length+i-1] = table[i+1][length+i-2] and (s[i] == s[length+i-1])
                    if table[i][length+i-1] and length >= len(substring):
                        substring = s[i:length+i]

            length = length + 1

        return substring
