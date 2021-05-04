#DFS: use Stack (LIFO), O(N), N = # of vertex

def dfs(graph,v,visited):
    # current node visited
    visited[v] = True
    print(v,end = ' ')
    # visit adjacent vertex recursively
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

