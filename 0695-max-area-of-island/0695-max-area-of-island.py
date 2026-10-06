class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        from collections import deque
        q=deque()
        r=len(grid)
        c=len(grid[0])
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        ans=0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    q.append((i,j)) 
                    grid[i][j]=0
                count=0
                while q:
                    ro,co=q.popleft()
                    count+=1
                    for dr,dc in directions:
                        nr=dr+ro
                        nc=dc+co
                        if 0<=nr<r and 0<=nc<c and grid[nr][nc]==1:
                            grid[nr][nc]=0
                            q.append((nr,nc))
                        
                    ans=max(count,ans)
                    
        return ans

