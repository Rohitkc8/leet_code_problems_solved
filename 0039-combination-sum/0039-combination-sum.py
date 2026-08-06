class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        ans=[]
        def rec(ind,sum_,sol):
            nonlocal res
            if ind>=len(candidates) or ind<0:
                return False

            if sum_==target:
                res.append(sol.copy())
                return False

            if sum_>target:
                return False

            sol.append(candidates[ind])
            
            rec(ind,sum_+candidates[ind],sol)

            sol.pop()
            rec(ind+1,sum_,sol)
        rec(0,0,[])
        return res
