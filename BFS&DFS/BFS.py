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
        print(v)
        for i in graph(v):
            if not visited[i]:
                queue.append(i)
                visited[i] = True