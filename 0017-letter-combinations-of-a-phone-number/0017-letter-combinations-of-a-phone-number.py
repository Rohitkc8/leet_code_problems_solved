class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        dicc={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tvu",
            "9":"wxyz"
        } 
        def bac(ind,sol):
            if len(sol)==len(digits):
                ans.append(sol)
                return
            if len(sol)>len(digits):
                return
            letters=dicc[digits[ind]]
            for ch in letters:
                bac(ind+1,sol+ch)
        bac(0,"")
        return ans