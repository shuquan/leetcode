class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = {}
        length = i = j = 0
        while i < len(s) and j < len(s):
            if s[j] not in substring:
                substring[s[j]] = 1
                j = j + 1
                length = max(length, len(substring))
            else:
                substring.pop(s[i])
                i = i + 1
        return length


    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ''
        length = i = j = 0
        while i < len(s) and j < len(s):
            if s[j] not in substring:
                substring = substring + s[j]
                j = j + 1
                length = max(length, len(substring))
            else:
                substring = substring[1:]
                i = i + 1
        return length
