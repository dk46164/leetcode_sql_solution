from collections import defaultdict

class Solution:
    def dfs(self,graph,src_nd,tgt_nd):
        # track node visited 
        visited = set()

        # define wrapper
        def wrapper(src_nd):
            # loop through each elements
            for key in graph[src_nd]:
                if key not in visited:
                    visited.add(key)
                    wrapper(key)
        
        # call function
        wrapper(src_nd)

        return True if src_nd in visited and tgt_nd in visited else False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # create graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # call dfs func
        return self.dfs(graph,source,destination) if graph else True 


        