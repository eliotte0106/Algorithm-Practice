#runtime: O(N^3), dp

INF = int(1e9) #infinity

#number of nodes and edges
n = int(input())
m = int(input())

# 2 X 2 list (graph), value of inf
graph = [[INF] * (n+1) for _ in range(n+1)]

#from a node to itself costs 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#info of edge
for _ in range(m):
    #from a to b cost c
    a,b,c = map(int,input().split())
    graph[a][b] = c

#from the equation
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

#print
for a in range(1,n+1):
    for b in range(1,n+1):
        #if inf
        if graph[a][b] == INF:
            print("infinity")
        else:
            print(graph[a][b], end = " ")
    print()
    

