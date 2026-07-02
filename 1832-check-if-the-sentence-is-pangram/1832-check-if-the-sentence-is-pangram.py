class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq={}
        for i in sentence:
            freq[i]=freq.get(i,0)+1
        if (len(freq))==26:
            return True
        return False
