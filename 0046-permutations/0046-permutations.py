class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used=[0]*(len(nums))
        ans=[]
        def bac(sol):
            if len(sol)==len(nums):
                ans.append(sol.copy())
                return
            for i in range(len(nums)):
                if used[i]==1:
                    continue
                used[i]=1
                sol.append(nums[i])
                bac(sol)
                used[i]=0
                sol.pop()
        bac([])
        return ans
            