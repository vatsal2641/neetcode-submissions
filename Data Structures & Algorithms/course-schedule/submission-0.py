class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\

        graph = [[] for i in range(numCourses)]

        for i,j in prerequisites:
            graph[j].append(i)

        visited = [False]*numCourses
        active_g = [False]*numCourses

        for v in range(numCourses):
            if not visited[v]:    #For starting the new dfs if the chain is broken.
                if self.DFS(graph, v, visited, active_g):
                    return False
        
        return True

    def DFS(self, graph, s, visited, active_g):

        visited[s] = True
        active_g[s] = True

        for v in graph[s]:
            if not visited[v]:
                if self.DFS(graph, v, visited, active_g):
                    return True
            elif active_g[v]:
                return True

        active_g[s] = False

        return False
