"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curStr = ""

        def dfs(curStr, left, right, n):
            if left < n:
                dfs(curStr + '(', left + 1, right, n)
            if left > right:
                dfs(curStr + ')', left, right + 1, n)
            if left == right == n:
                result.append(curStr)
            return 0

        dfs(curStr, 0, 0, n)
        return result
