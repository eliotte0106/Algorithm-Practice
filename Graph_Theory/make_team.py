"""
1. 0 ~ N numbers
2. N+1 teams

rules: 1. team union : making 2 teams to 1 team
            form: 0 a b
       2. same team : checking if 2 students are in a same team
            form: 1 a b
"""
def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper,a,b = map(int,input().split())
    #if union
    if oper == 0:
        union_parent(parent,a,b)
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("yes")
        else:
            print("no")