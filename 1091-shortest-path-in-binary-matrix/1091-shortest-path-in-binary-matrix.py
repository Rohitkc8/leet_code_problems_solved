class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        from collections import deque
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        q=deque([(0,0,1)])
        n=len(grid)
        m=len(grid[0])
        if grid[0][0]==1:
            return -1
        while q:
            r,c,p=q.popleft()
            if r==m-1 and c==n-1:
                return p
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    q.append((nr,nc,p+1))
        return -1
        

            