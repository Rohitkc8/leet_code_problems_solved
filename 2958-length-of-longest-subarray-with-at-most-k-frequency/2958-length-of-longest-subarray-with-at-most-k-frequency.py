class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        freq={}
        ans=0
        while(r<len(nums)):
            freq[nums[r]]=freq.get(nums[r],0)+1

            while(freq[nums[r]]>k):
                freq[nums[l]]-=1
                l+=1
            
            ans=max(ans,r-l+1)
            r+=1
        return ans
