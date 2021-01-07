class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        result = 0
        charList = [-1] * 256
        while right < len(s):
            left = max(left, charList[ord(s[right])] + 1)
            charList[ord(s[right])] = right
            right += 1
            result = max(result, right - left)
        return result
            