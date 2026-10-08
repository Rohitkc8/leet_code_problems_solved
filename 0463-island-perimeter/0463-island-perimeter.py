class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter
            if r >= m or c >= n or r < 0 or c < 0 or grid[r][c] == 0:
                perimeter += 1
                return
            if grid[r][c] == -1:
                return
            grid[r][c] = -1
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)

        return perimeter