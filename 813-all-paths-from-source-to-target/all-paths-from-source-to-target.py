class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]):

        def dfs(graph,src_nd,tgt_nd,path):
            if src_nd==tgt_nd:
                yield path
            
            for node in graph[src_nd]:
                yield from dfs(graph,node,tgt_nd,path+[node])

        graph_adj = {u:set(ngh) for u,ngh in enumerate(graph)}

        return list(dfs(graph,0,len(graph)-1,[0]))

        
        