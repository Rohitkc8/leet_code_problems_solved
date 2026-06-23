class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        s=[]
        while(len(word1)>i and len(word2)>j):
            s.append(word1[i])
            s.append(word2[j])
            i=i+1
            j=j+1
        while(len(word1)>i):
            s.append(word1[i])
            i=i+1
        while(len(word2)>j):
            s.append(word2[j])
            j=j+1
        return ''.join(s)
        