class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        visited = set()
        
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
      

        def dfs(ele, parent):
            visited.add(ele)

            for v in adj[ele]:
                print(v, visited)
                if v not in visited:
                    if dfs(v, ele) is False:
                        return False
                
                elif v!=parent:
                    return False
        count = 0

        for u in range(n):
            if u not in visited:
                count+=1
                if dfs(u, -1) == False:
                    return False
            
        if count>1:
            return False
            
        return True