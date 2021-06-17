#runtime : O(V+E)

from collections import deque

#nodes and edges
v,e = map(int,input().split())

#indegree set
indegree = [0] * (v+1)

#edge info in adjacency list (graph)
graph = [[] for i in range(v+1)]

#info of edge from directed graph
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

#topology sort function
def topology_sort():
    result = []
    q = deque()

    #at first, the node which has indegree of 0 into queue
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    #until queue is empty
    while q:
        now = q.popleft()
        result.append(now)

        #connected nodes from now gets indegree - 1
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i,end= " ")

topology_sort()