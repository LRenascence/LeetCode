"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = re.split(" ", s)
        for i in range(len(wordList) - 1, -1, -1):
            if wordList[i]:
                return len(wordList[i])
        return 0