'''
Count the number of moves to get out of maze.
The escape hole is positioned at N,M.
*Starting from the first row and first column.
ex)
110
010
011
should output 5
'''

from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0] #up,down
dy=[0,0,-1,1]#left,right

def bfs(x,y):
    queue = deque() #deque lib
    queue.append((x,y))
    while queue: #while empty
        x,y = queue.popleft()
        for i in range(4): #check directions of up,down,left,right
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: #out of bound
                continue
            if graph[nx][ny] == 0: #if wall is 0
                continue
            if graph[nx][ny] == 1: #node is visited for the first time,
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1] #the most right under vertex

print(bfs(0,0))
