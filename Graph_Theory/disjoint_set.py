#use tree data structure to find disjoint_sets
#smaller node becomes the root node

#find the set that includes a particular element
def find_parent(parent, x):
    #if not a root node, recursive call until find the root node
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x] #path compression

#union the set that includes two elements
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

#input of num of nodes and edges(union)
v,e = map(int,input().split())
parent = [0] * (v+1) #parent table

#parent table
for i in range(1,v+1):
    parent[i] = i

#union process
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

#print the set that each element in included
# + important thing is from calling find_parent in this loop, checks the parent table again and finalize the parent table. +
print("set of each element: ", end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

#print parent table
print("parent table: ",end='')
for i in range(1, v+1):
    print(parent[i],end=' ')

