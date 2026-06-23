class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        fre={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in t:
            fre[i]=fre.get(i,0)+1
        
        print(freq)
        print(fre)
        if freq==fre:
            return True
        return False