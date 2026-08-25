class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        v=k
        while v in s:
            v+=k
        return v


        