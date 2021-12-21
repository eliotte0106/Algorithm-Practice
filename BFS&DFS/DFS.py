#DFS: use Stack (LIFO), O(N), N = # of vertex

def dfs(graph, v, visited):
    # current node visited
    visited[v] = True
    print(v,end = ' ')
    # visit adjacent vertex recursively
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#example
visited = [False] * 9
graph = [[], [2,3,8], [1,7,8], [1,4,5], [3,5], [3,4], [7], [6,8], [1,7]]
dfs(graph, 1, visited)

#1 2 7 6 8 3 4 5