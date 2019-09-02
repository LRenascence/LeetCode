"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        N = len(beginWord)
        #build neighborhood
        wordDict = {}
        wordList = set(wordList) | set([beginWord])
        for word in wordList:
            for i in range(N):
                string = word[:i] + '_' + word[i + 1:]
                wordDict[string] = wordDict.get(string, []) + [word]
        
        #BFS
        bfsList = [(beginWord, 1)]
        visited = set()
        while bfsList:
            curWord, length = bfsList.pop(0)
            if curWord == endWord:
                    return length
            if curWord not in visited:
                visited.add(curWord)
                for i in range(N):
                    string = curWord[:i] + '_' + curWord[i + 1:]
                    for neigh in wordDict[string]:
                        if neigh not in visited:
                            bfsList.append((neigh, length + 1))
        return 0