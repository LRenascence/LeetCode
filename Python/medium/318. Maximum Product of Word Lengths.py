"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
 

Constraints:

0 <= words.length <= 10^3
0 <= words[i].length <= 10^3
words[i] consists only of lowercase English letters.
"""
# slow
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) <= 1:
            return 0
        words = sorted(words, key = lambda x : len(x), reverse = True)
        result = 0
        for i in range(len(words) - 1):
            letterSet = set()
            for letter in words[i]:
                letterSet.add(letter)
            for j in range(i + 1, len(words)):
                foundSameLetter = False
                for letter in words[j]:
                    if letter in letterSet:
                        foundSameLetter = True
                        break
                if not foundSameLetter:
                    result = max(result, len(words[i]) * len(words[j]))
        return result

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) <= 1:
            return 0
        bitList = []
        for word in words:
            tempBit = 0
            for letter in word:
                tempBit |= 1 << (ord(letter) - ord('a'))
            bitList.append(tempBit)
        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitList[i] & bitList[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result