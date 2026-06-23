class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d = {")":"(","}":"{","]":"["}
        for i in s:
            if i in "({[":
                l.append(i)
            elif l and d[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        if l:
            return False
        else:
            return True