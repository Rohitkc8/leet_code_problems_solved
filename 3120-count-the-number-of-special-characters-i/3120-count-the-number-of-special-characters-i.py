class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        p=[]
        q=[]
        c=0
        for i in word:
            if i.islower():
                if i not in p:
                    p.append(i)
            if i.isupper():
                if i not in q:
                    q.append(i)
        for i in p:
            if i.upper() in q:
                c+=1
        return c
                
