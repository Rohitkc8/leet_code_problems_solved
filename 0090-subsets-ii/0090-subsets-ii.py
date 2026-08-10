class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def rec(ind,sol):
            nonlocal ans
            ans.append(sol.copy())
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                sol.append(nums[i])
                rec(i+1,sol)
                sol.pop()
        rec(0,[])
        return ans
