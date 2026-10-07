class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n=len(isConnected)
        visited=[False]*(n)
        provinces=0
        def dfs(city):
            visited[city]=True
            for neigh in range(n):
                if isConnected[city][neigh] and not visited[neigh]:
                    dfs(neigh)
        
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces+=1
        return provinces
