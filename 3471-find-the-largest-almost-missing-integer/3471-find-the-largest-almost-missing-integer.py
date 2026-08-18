class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        freq={}
        while(r<len(nums)):
            if r-l>=k:
                l+=1
            r+=1
            if len(nums[l:r])==k:
                for i in set(nums[l:r]):
                    freq[i]=freq.get(i,0)+1
        max_=-1
        for i,j in freq.items():
            if j==1:
                max_=max(max_,i)
        return max_