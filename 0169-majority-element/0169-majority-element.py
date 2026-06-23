class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        max=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
        print(freq)
        for i in freq:
            if(freq[i]>max):
                max=freq[i]
        for i in freq:
            if max==freq[i]:
                return i

            
