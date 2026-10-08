class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        from collections import deque
        q=deque()
        dis=[[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dis[i][j]=0
                    q.append((i,j))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        ans=-1
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<m and 0<=nc<n and dis[nr][nc]==-1:
                    dis[nr][nc]=dis[r][c]+1
                    ans=max(ans,dis[nr][nc])
                    q.append((nr,nc))
        
        return ans
