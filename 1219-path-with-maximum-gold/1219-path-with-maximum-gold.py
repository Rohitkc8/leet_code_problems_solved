class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        ans=0
        sol=[[0]*(c) for _ in range(r)]
        def bac(x,y,sol,gold):
            nonlocal ans

            if x>r-1 or y>c-1 or x<0 or y<0 or sol[x][y]==1:
                return
            if grid[x][y]==0:
                return

            gold+=grid[x][y]
            ans=max(ans,gold)
            sol[x][y]=1

            bac(x,y-1,sol,gold)
            bac(x+1,y,sol,gold)
            bac(x-1,y,sol,gold)
            bac(x,y+1,sol,gold)

            sol[x][y]=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=0:
                    bac(i,j,sol,0)
        return ans