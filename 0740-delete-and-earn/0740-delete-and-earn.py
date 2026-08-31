class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        if not nums:
            return 0
        else:

            n = max(nums)
            dp = [0] * (n + 1)

            for i in nums:
                dp[i] += i

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])

            return dp[n]

