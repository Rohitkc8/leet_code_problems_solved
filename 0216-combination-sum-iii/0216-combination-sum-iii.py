class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def bac(ind,sol):
            nonlocal ans
        
            if sum(sol)>n or len(sol)>k:
                return
            if sum(sol)==n and len(sol)==k:
                ans.append(sol.copy())
                return
            if ind>9:
                return
            sol.append(ind)
            bac(ind+1,sol)

            sol.pop()
            bac(ind+1,sol)
    
        bac(1,[])
        return ans