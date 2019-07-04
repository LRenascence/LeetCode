"""
similar questions
https://leetcode.com/problems/minimum-window-substring/
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

# s is the longer string, t is the shorter sting
def sildingWindow(s, t):
    # init variables
    result = []
    charDict = {}

    # init charDict
    for i in t:
        if i not in charDict:
            charDict[i] = 0
        charDict[i] += 1

    begin = end = 0
    count = len(charDict)

    # search string s
    while end < len(s):
        endChar = s[end]
        if endChar in charDict:
            charDict[endChar] -= 1
            if charDict[endChar] == 0:
                count -= 1
        end += 1

        while count == 0:
            beginChar = s[begin]
            if beginChar in charDict:
                charDict[beginChar] += 1
                if charDict[beginChar] > 0:
                    count += 1

            if end - begin == len(t):
                result.append(begin)

    return result