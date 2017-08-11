class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        dp=[None]*len(nums)
        max_so_far = dp[0] = nums[0]
        for i,e in enumerate(nums):
            if i > 0:
                dp[i] = max(e,e+dp[i-1])
            max_so_far = max(max_so_far, dp[i])
        return max_so_far
