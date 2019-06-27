"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = {}
        for i in s:
            if i not in charDict:
                charDict[i] = 0
            charDict[i] += 1
        length = 0
        for i in charDict:
            while charDict[i] >= 2:
                charDict[i] -= 2
                length += 2
        if length < len(s):
            length += 1
        return length


# another edition
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = {}
        length = 0
        for i in s:
            if i not in charDict:
                charDict[i] = 0
            charDict[i] += 1
            if charDict[i] >= 2:
                charDict[i]  -= 2
                length += 2
        if length < len(s):
            length += 1
        return length
