#BFS : Use Queue(FIFO), O(N) N = # of vertex, usually faster than DFS.

from collections import deque

def bfs(graph,start,visited):
    #use deque library
    queue = deque([start])
    #current node visited
    visited[start] = True
    # until queue is empty
    while queue:
        #print
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
graph = [[], [2,3,8], [1,7,8], [1,4,5], [3,5], [3,4], [7], [6,8], [1,7]]
bfs(graph, 1, visited)

#1 2 3 8 7 4 5 6