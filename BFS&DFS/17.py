from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])



"""
input:
3 3
1 0 2
0 0 0
3 0 0
2 3 2

output:
3
"""

"""
process:

initial)
1 0 2
0 0 0
3 0 0

step1)
1 1 2
1 0 2
3 3 0

step2)
1 1 2
1 1 2
3 *3* 2
"""