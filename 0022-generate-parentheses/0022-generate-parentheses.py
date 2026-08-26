class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def bac(open_c,close_c,s):
            if len(s)==n*2:
                ans.append(s)
                return
            if open_c<n:
                bac(open_c+1,close_c,s+"(")
            if close_c<open_c:
                bac(open_c,close_c+1,s+")")

        bac(0,0,"")
        return ans