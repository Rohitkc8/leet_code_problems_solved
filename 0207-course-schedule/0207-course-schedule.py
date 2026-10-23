class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses
        from collections import deque
        q=deque()
        for a,b in prerequisites:
            graph[b].append(a)
            indgree[a]+=1
        for i in range(numCourses):
            if indgree[i]==0:
                q.append(i)
        c=0
        while q:
            node=q.popleft()
            c+=1
            for nei in graph[node]:
                indgree[nei]-=1
                if indgree[nei]==0:
                    q.append(nei)
        return c==numCourses
        
        