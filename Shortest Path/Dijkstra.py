#runtime : O(ElogV), using heapq(priority queue), greedy

import heapq
import sys
input = sys.stdin.readline #faster
INF = int(1e9) #infinity

#number of nodes and edges
n, m = map(int,input().split())
#start node
start = int(input())
#info of connected nodes
graph = [[] for i in range(n+1)]
#distance set as infinity
distance = [INF] * (n + 1)

#all edge info
for _ in range(m):
    a, b, c = map(int,input().split())
    #from a to b, cost is c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    #to go to the first node, the distance is 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #if q is not empty
        #bring info of the node of shortest distance
        dist, now = heapq.heappop(q)
        #if current node is processed, ignore
        if distance[now] < dist:
            continue
        #check adjacent nodes
        for i in graph[now]:
            cost = dist + i[1]
            #if the distance to other node is shorter,
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])