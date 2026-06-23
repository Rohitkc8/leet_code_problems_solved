class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while(i<j):
            if s[i] not in a:
                i=i+1
            if s[j] not in a:
                j=j-1
            if s[i] in a and s[j] in a:
                s[i],s[j]=s[j],s[i]
                i=i+1
                j=j-1
        return "".join(s)