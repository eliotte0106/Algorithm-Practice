#find the set of a particular element
def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#union the set of 2 elements
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

#input of num of nodes and edges(#union)
v,e = map(int,input().split())
parent = [0] * (v + 1) # parent table

#parent table
for i in range(1,v+1):
    parent[i] = i

#cycle
cycle = False

for i in range(e):
    a, b = map(int,input().split())
    #if cycle, terminate
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("cycle appeared")
else:
    print("cycle not appeared")


