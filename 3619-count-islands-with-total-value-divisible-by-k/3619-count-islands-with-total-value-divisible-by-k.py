class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        from collections import deque
        q=deque()
        m=len(grid)
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        sum_=0
        n=len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    q.append((i,j))
                    if sum_%k==0:
                        ans+=1
                    sum_=grid[i][j]
                    grid[i][j]=0
                while q:
                    r,c=q.popleft()
                    for dr,dc in directions:
                        nr=dr+r
                        nc=dc+c
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc]!=0:
                            sum_+=grid[nr][nc]
                            grid[nr][nc]=0
                            q.append((nr,nc))
        if sum_%k==0:
            ans+=1
        return ans-1
          

            
        