class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum_ = 0
        ans = float("inf")
        r=0
        while(r<len(nums)):
            sum_ += nums[r]
            r+=1
            while sum_ >= target:
                ans = min(ans, r - l)
                sum_ -= nums[l]
                l += 1

        return 0 if ans == float("inf") else ans