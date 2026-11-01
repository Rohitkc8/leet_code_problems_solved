class Solution(object):
    def minMoves(self, nums):
        min_=min(nums)
        ans=0
        for i in range(len(nums)):
            ans+=nums[i]-min_
            
            
        return ans
        