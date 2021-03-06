"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        index = 0
        while index < len(s):
            if index + k >= len(s):
                if index != 0:
                    s[index:] = s[len(s) - 1: index - 1: -1]
                else:
                    s[index:] = s[len(s) - 1:: -1]
                break
            if index != 0:
                s[index: index + k] = s[index + k - 1: index - 1: -1]
            else:
                s[index: index + k] = s[index + k - 1:: -1]
            index += 2 * k
        return "".join(s)