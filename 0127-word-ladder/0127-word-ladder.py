class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        from collections import deque
        q=deque([(beginWord,1)])
        words=set(wordList)
        if beginWord in words:
            words.remove(beginWord)
        letters="abcdefghijklmnopqrstuvwxyz"
        while q:
            word,s=q.popleft()
            if word==endWord:
                return s
            for i in range(len(word)):
                for j in letters:
                    newword=word[:i]+j+word[i+1:]
                    if newword in words:
                        q.append((newword,s+1))
                        words.remove(newword)
        return 0
        
            
                        