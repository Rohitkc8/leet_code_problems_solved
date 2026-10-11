
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        path_visited = [0] * numCourses
        visited = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):
            visited[node] = 1
            path_visited[node] = 1

            for nxt in graph[node]:
                if visited[nxt] == 0:
                    if dfs(nxt):
                        return True
                else:
                    if path_visited[nxt] == 1:
                        return True

            path_visited[node] = 0
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    return False

        return True
