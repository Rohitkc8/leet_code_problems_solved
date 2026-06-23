class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq1={}
        for i in s:
            freq1[i]=freq1.get(i,0)+1
        for i in t:
            freq1[i]=freq1.get(i,0)-1

        for key,value in freq1.items():
            if value!=0:
                return key
    