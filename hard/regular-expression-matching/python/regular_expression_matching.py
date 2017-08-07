class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_l = len(s)
        p_l = len(p)
        dp = [[None]*(p_l+1) for i in xrange(s_l+1)]

        dp[0][0] = True
        for i in xrange(p_l):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True
            else:
                dp[0][i+1] = False
        for i in xrange(s_l):
            dp[i+1][0] = False

        for i in xrange(s_l):
            for j in xrange(p_l):
                if p[j] == s[i] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] == s[i] or p[j-1] == '.':
                        # in this case, a* counts as singel a, multiple a or empty,
                        # such as
                        # 1) s='aba', p='aba*'
                        # 2) s='abaa', p='aba*'
                        # 3) s='aba', p='abaa*'
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
                    else:
                        # in this case, a* only counts as empty,
                        # such as s='abc', p='abcd*'
                        dp[i+1][j+1] = dp[i+1][j-1]
                else:
                    dp[i+1][j+1] = False

        return dp[s_l][p_l]

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_l = len(s)
        p_l = len(p)
        dp = [[None]*(p_l+1) for i in xrange(s_l+1)]

        dp[0][0] = True
        for i in xrange(p_l):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True
            else:
                dp[0][i+1] = False
        for i in xrange(s_l):
            dp[i+1][0] = False

        for i in xrange(s_l):
            for j in xrange(p_l):
                if p[j] == s[i] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    # in this case, a* only counts as empty
                    if s[i] != p[j-1] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    # in this case, a* counts as single a, multiple a or empty
                    else:
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
                else:
                    dp[i+1][j+1] = False

        return dp[s_l][p_l]
