class Solution:
    def reverseWords(self, s: str) -> str:
        y=" "
        arr=s.split()
        arr=arr[::-1]
        for i in arr:
            y=y+i+" "
            y.strip()
        return y[1:-1]
            