class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        v="aeiouAEIOU"
        while(i<j):
            if s[i] not in v:
                i=i+1
            if s[j] not in v:
                j=j-1
            if s[i] in v and s[j] in v:
                s[i],s[j]=s[j],s[i]
                i=i+1
                j=j-1
        return "".join(s)