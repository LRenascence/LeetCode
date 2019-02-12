"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.KMP(haystack, needle)

    def KMP(self, string, subString):
        # special situation
        if not subString:
            return 0
        # build subString table first
        index = 0  # length of the previous longest prefix suffix
        subStringTable = [0] * len(subString)
        i = 1
        # the loop calculates lps[i] for i = 1 to M-1
        while i < len(subString):
            if subString[i] == subString[index]:
                index += 1
                subStringTable[i] = index
                i += 1
            else:
                if index != 0:
                    index = subStringTable[index - 1]

                    # Also, note that we do not increment i here
                else:
                    subStringTable[i] = 0
                    i += 1
        # search subString in string
        i = 0
        j = 0
        while i < len(string):
            if string[i] == subString[j]:
                i += 1
                j += 1
                if j == len(subString):
                    return i - j
            else:
                if j == 0:
                    i += 1
                    continue
                j = subStringTable[j - 1]
        return -1