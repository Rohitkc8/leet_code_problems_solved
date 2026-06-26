class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r=l=0
        p=0
        freq={}
        while(r<len(fruits)):
            freq[fruits[r]]=freq.get(fruits[r],0)+1
            r+=1
            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    freq.pop(fruits[l])
                l+=1
            print(freq)
            p=max(p,r-l)
        return p

        