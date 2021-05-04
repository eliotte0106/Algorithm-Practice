'''
Snake game
'''

n = int(input())
k = int(input())
data = [[0]* (n+1) for _ in range(n+1)] # map info
info = [] # rotation info

#map info (if apple is there, indicated as 1)
for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1 # apple position

#rotation info
l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

# E,S,W,N
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction
def simulate():
    x,y = 1,1 # snake position
    data[x][y] = 2 # indicate snake's position as 2
    direction = 0 # looking east first
    time = 0 # time
    index = 0 # next rotation info
    q = [(x,y)] # snake pos info (x is tail)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # if in the map and 
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            #if there is no apple, move and remove tail
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
            #if there is an apple, remain tail
            if data[nx][ny] == 1: 
                data[nx][ny] = 2
                q.append((nx,ny))
            #if snake meets the wall, crash
        else:
            time += 1
            break
        x,y = nx,ny # next position
        time += 1
        if index < l and time == info[index][0]: # if rotating time, rotate
            direction = turn(direction,info[index][1])
            index += 1
    return time

print(simulate())
