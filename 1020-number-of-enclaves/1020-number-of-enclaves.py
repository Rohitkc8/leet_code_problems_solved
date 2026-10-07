class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        def dfs(r,c):
            if r>=m or c>=n or r<0 or c<0 or grid[r][c]==0:
                return

            grid[r][c]=0
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(n):
            if grid[0][i]==1:
                dfs(0,i)
            if grid[m-1][i]==1:
                dfs(m-1,i)
        for i in range(m):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][n-1]==1:
                dfs(i,n-1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans+=1
        return ans