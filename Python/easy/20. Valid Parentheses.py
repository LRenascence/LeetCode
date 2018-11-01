"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:
Input: "(]"
Output: false
Example 4:
Input: "([)]"
Output: false
Example 5:
Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        rightPart = [']', ')', '}']
        leftPart = ['[', '(', '{']
        for i in range(len(s) - 1, -1, -1):
            if s[i] in rightPart:
                lst.append(s[i])
            if s[i] in leftPart:
                if lst == []:
                    return False
                if s[i] == leftPart[rightPart.index(lst[-1])]:
                    lst.pop()
                else:
                    return False
        if lst != []:
            return False
        return True