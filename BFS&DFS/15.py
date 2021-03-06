from collections import deque

#num of cities, num of roads, distance info, num of starting city
n,m,k,x = map(int,input().split())
graph = [[]for _ in range(n+1)] # 2중 list declare

#roads info
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

#BFS
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

#print ascending of num of cities that have shortest distance K
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

#ex :4 4 2 1
#   1 2
#   1 3
#   2 3
#   2 4
#output : 4 
