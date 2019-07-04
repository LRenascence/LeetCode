"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        charDict = {}
        for i in p:
            if i not in charDict:
                charDict[i] = 0
            charDict[i] += 1
        begin = end = 0
        count = len(charDict)
        result = []

        while end < len(s):
            letter = s[end]
            if letter in charDict:
                charDict[letter] -= 1
                if charDict[letter] == 0:
                    count -= 1
            end += 1

            while count == 0:
                tempLetter = s[begin]
                if tempLetter in charDict:
                    charDict[tempLetter] += 1
                    if charDict[tempLetter] > 0:
                        count += 1
                if end - begin == len(p):
                    result.append(begin)
                begin += 1

        return result