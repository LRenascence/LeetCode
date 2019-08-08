"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            tempDict = {}
            for j in i:
                if j not in tempDict:
                    tempDict[j] = 0
                tempDict[j] += 1
            letterStr = ['0'] * 26
            for j in tempDict:
                letterStr[ord(j) - 97] = str(tempDict[j])
            letterStr = ''.join(letterStr)
            if letterStr not in dic:
                dic[letterStr] = []
            dic[letterStr].append(i)
        result = []
        for i in dic:
            result.append(dic[i])
        return result

# better
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            key = tuple(sorted(i))

            dic[key] = dic.get(key, []) + [i]
        return dic.values()