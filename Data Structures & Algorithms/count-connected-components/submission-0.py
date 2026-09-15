class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connected_comp= 0 

        visited = [0]*n

        adj = [[] for i in range(n)]

        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(v):
            visited[v] = True
            for u in adj[v]:
                if not visited[u]:
                    dfs(u)
            return

        for i in range(n):
            
            if not visited[i]:
        
                dfs(i)
                connected_comp +=1

    
        return connected_comp