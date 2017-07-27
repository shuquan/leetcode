class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i,e in enumerate(nums):
            if e in hash_map:
                return [hash_map[e], i]
            else:
                hash_map[target - e] = i

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,e in enumerate(nums, 1):
            x = target - e
            if x in nums and x in nums[i:]:
                return nums.index(e), nums[i:].index(x) + i
