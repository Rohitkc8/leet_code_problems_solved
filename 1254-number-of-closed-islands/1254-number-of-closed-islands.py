class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        from collections import deque
        q=deque()
        m=len(grid)
        n=len(grid[0])
        for i in range(n):
            if grid[0][i]==0:
                grid[0][i]=1
                q.append((0,i))
            if grid[m-1][i]==0:
                grid[m-1][i]=1
                q.append((m-1,i))
        for i in range(m):
            if grid[i][0]==0:
                grid[i][0]=1
                q.append((i,0))
            if grid[i][n-1]==0:
                grid[i][n-1]=1
                q.append((i,n-1))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    q.append((nr,nc))
        iseland=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
                    iseland+=1
                while q:
                    ro,co=q.popleft()
                    for dr,dc in directions:
                        nr=dr+ro
                        nc=dc+co
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc]==0:
                            grid[nr][nc]=1
                            q.append((nr,nc))
        return iseland

        
            
