class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        from collections import deque
        q=deque()
        n=len(mat)
        m=len(mat[0])
        dis=[[-1]*(m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j))
                    dis[i][j]=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c

                if 0<=nr<n and 0<=nc<m and dis[nr][nc]==-1:
                    dis[nr][nc]=dis[r][c]+1
                    q.append((nr,nc))
        return dis
