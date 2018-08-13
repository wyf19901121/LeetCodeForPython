class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        index = {}
        left = 0
        right = 0
        maxLen = 0

        while right < len(s):
            if s[right] in index and index[s[right]] >= left:
               maxLen = maxLen if maxLen >= right - left else right - left
               left = index[s[right]] + 1
            index[s[right]] = right
            right += 1
        maxLen = maxLen if maxLen >= right - left else right - left

        return maxLen



