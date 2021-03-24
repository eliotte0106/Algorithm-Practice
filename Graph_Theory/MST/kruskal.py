#find a set of a particular element
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#union
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#input of #nodes and #edges
v,e = map(int,input().split())
parent = [0] * (v+1) #parent table

#list and result
edges = []
result = 0

#parent table
for i in range(1,v+1):
    parent[i] = i

#edge info
for _ in range(e):
    a, b, cost = map(int,input().split())
    #using tuple to sort by cost
    edges.append((cost,a,b))

edges.sort()

#checking edge
for edge in edges:
    cost, a, b = edge
    #if not cycle, union
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        
print(result)