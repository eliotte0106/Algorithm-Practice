'''
From city A, find total number of cities and time that cities receive a letter from A.
Conditions: connected cities from A can receive a letter even if not adjacent.

ex)
3 cities, 2 paths, start city : 1

From 1 to 2, takes 4 time
1   2   4
1   3   2
output should be 2, 4

'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)

print(count-1,max_distance)