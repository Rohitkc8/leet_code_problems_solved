class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r=0
        l=0
        max_count=0
        coun_0=0
        coun_1=0
        while(r<len(nums)):
            if nums[r]==1:
                coun_1+=1
            else:
                coun_0+=1
                while(coun_0>k):
                    if nums[l]==1:
                        coun_1-=1
                    else:
                        coun_0-=1
                    l=l+1
            max_count=max(max_count,r-l+1)
            r=r+1
        return max_count