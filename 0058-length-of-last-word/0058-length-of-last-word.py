class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        s=s[::-1].strip()
        for i in s:
            if(i!=" "):
                c=c+1
            else:
                break
        return c
        