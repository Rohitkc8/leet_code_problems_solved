class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        from collections import deque
        q=deque()
        indgree=[0]*(numCourses)
        adj=[[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[b].append(a)
            indgree[a]+=1
        for i in range(numCourses):
            if indgree[i]==0:
                q.append(i)
        print(adj)
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indgree[nei]-=1
                if indgree[nei]==0:
                    q.append(nei)
        if len(ans)==numCourses:
            return ans
        return []

        
            
        