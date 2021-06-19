'''
There are N houses and M streets. Each houses are connected with the light with the cost.
Find the waste of cost.
'''
# kruskal algorithm 

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def find_union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int,input().split()) #num of house, num of street

parent = [0] * (n+1)
street = []
result = 0
no_use = 0

for i in range(n):
    parent[i] = i

for i in range(m):
    x,y,z = map(int,input().split()) #house1,house2,cost
    street.append((z,x,y))
    result += z

street.sort()

for info in street:
    z,x,y = info
    if find_parent(parent,x) != find_parent(parent,y):
        find_union(parent,x,y)
        no_use += z
        
print(result)
print(no_use)
print(result - no_use)