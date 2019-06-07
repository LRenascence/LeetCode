"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
# easy solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}
        for i in ransomNote:
            if i not in ransomDict:
                ransomDict[i] = 0
            ransomDict[i] += 1
        for i in magazine:
            if i not in magazineDict:
                magazineDict[i] = 0
            magazineDict[i] += 1
        for i in ransomNote:
            if i not in magazineDict:
                return False
            if ransomDict[i] > magazineDict[i]:
                return False
        return True

# a little improvement
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}
        for i in magazine:
            if i not in magazineDict:
                magazineDict[i] = 0
            magazineDict[i] += 1
        for i in ransomNote:
            if i not in magazineDict:
                return False
            if magazineDict[i] == 0:
                return False
            magazineDict[i] -= 1
        return True

