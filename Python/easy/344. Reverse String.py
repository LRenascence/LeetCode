"""
Write a function that takes a string as input and returns the string reversed.
Example 1:
Input: "hello"
Output: "olleh"
Example 2:
Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(int(len(s) / 2)):
            s[i], s[~i] = s[~i], s[i]
        return "".join(s)