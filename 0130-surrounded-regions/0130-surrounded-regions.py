class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m=len(board)
        n=len(board[0])
        def dfs(r,c):
            if r>=m or c>=n or r<0 or c<0:
                return
            if board[r][c]!="O":
                return
            board[r][c]="#"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(n):
            if board[0][i]=="O":
                dfs(0,i)
            if board[m-1][i]=="O":
                dfs(m-1,i)

        for  i in range(m):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][n-1]=="O":
                dfs(i,n-1)
            
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="#":
                    board[i][j]="O"