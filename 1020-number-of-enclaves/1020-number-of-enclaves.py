class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        from collections import deque
        q=deque()
           
        for i in range(n):
            if grid[0][i]==1:
                grid[0][i]=0
                q.append((0,i))
            if grid[m-1][i]==1:
                grid[m-1][i]=0
                q.append((m-1,i))

        for i in range(m):
            if grid[i][0]==1:
                grid[i][0]=0
                q.append((i,0))
            if grid[i][n-1]==1:
                grid[i][n-1]=0
                q.append((i,n-1))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<m and 0<=nc<n:
                    if grid[nr][nc]==1:
                        grid[nr][nc]=0
                        q.append((nr,nc))

            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans+=1
        return ans