'''
There is a map N * N. A person starts from 1,1.
By the instructions by using L,R,U,D.
Find the output of the final destination.
ex) RRRUDD should be output 3 4
'''

n = int(input("enter the size n for a map: "))
x,y = 1,1
paths = input().split()

move = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for path in paths:
    for i in range(len(move)):
        if path == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x,y = nx,ny
print(x,y)