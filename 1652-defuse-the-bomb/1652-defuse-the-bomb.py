class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        bom=code+code   
        ans=[0]*(len(code))
        n=len(code)
        if k==0:
            return ans
        if k>0:
            for i in range(len(code)):
                ans[i]=sum(bom[i+1:k+i+1])
            return ans
        
        if k<0:
            for i in range(len(code)):
                ans[i]=sum(bom[i + n + k : i + n])
            return ans
