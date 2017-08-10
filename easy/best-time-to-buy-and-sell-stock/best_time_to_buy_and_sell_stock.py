class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0

        l = len(prices)
        dp = [[None]*l for i in xrange(l)]

        for offset in xrange(l):
            for i in xrange(l):
                j = i + offset
                if offset == 0:
                    dp[i][j] = 0
                elif offset == 1 and j < l:
                    dp[i][j] = max(prices[j] - prices[i], 0)
                elif offset > 1 and j < l:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j], prices[j] - prices[i])

        return dp[0][l-1]

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0

        dp = []
        min_prices = prices[0]

        for i,e in enumerate(prices):
            min_prices = min(e, min_prices)
            if i == 0:
                dp.append(0)
            else:
                dp.append(max(e-min_prices, dp[i-1]))

        return dp[-1]
