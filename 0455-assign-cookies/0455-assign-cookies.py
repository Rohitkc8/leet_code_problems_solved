class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        c=0
        j=0
        while(i<len(g) and j<len(s)):
            if g[i]<=s[j]:
                j=j+1
                i=i+1
                c=c+1
            else:
                j+=1
        return c
       


