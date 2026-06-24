class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=len(s1)
        freq={}
        f=0
        for i in s1:
            freq[i]=freq.get(i,0)+1
        
        for i in range(len(s2)):
            freq1={}
            for i in s2[i:(i+a)]:
                freq1[i]=freq1.get(i,0)+1
            if freq==freq1:
                return True
                f=1
                break
        if f==0:
            return False
            