class Solution:
    def scoreOfString(self, s: str) -> int:
        p=[]
        for i in range(len(s)):
            p.append(abs(ord(s[i])-ord(s[i-1])))
        print(p)
        return sum(p[1:])
