class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        m=0
        n=0
        for i in range(len(nums)):
            if nums[i]<0:
                n=n+1
            elif nums[i]>0:
                m=m+1
        if m>n:
            return m
        else:
            return n