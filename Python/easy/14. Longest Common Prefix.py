"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
# My solution
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLength = 2**31
        count = 0
        flag = True
        rev = ""
        while flag:
            if strs == [] or strs[0] == "":
                break
            sameLetter = strs[0][count]
            for i in strs:
                if i == "":
                    flag = False
                    break
                # find min length
                if  count == 0:
                    if len(i) < minLength:
                        minLength = len(i)
                if i[count] != sameLetter:
                    flag = False
            count += 1
            if flag:
                rev +=sameLetter
            if count == minLength:
                break
        return rev


