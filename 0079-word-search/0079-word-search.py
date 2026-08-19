class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
    
        sol=[[0]*c for _ in range(r)]
        def bac(x,y,sol,s):
        
            if x>r-1 or y>c-1 or x<0 or y<0 or sol[x][y]==1:
                return
            if len(s)>=len(word):
                return
            if board[x][y]!=word[len(s)]:
                return
            s+=board[x][y]

            if s==word:
                return True
            
            sol[x][y]=1
            if bac(x,y+1,sol,s):
                return True
            if bac(x+1,y,sol,s):
                return True
            if bac(x,y-1,sol,s):
                return True
            if bac(x-1,y,sol,s):
                return True

            sol[x][y]=0
            return
        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    x=i
                    y=j
                    if bac(x,y,sol,""):
                        return True       
        
        return False