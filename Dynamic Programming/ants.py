"""
Find the sum of maximum food storage that are not located next to each other.
ex {1,3,1,5} -> can pick 3,5 
"""

# a_i = max(a_(i-1),a_(i-2)+k_i)

#bottom up approach (comparing i-1 and i-2)
n = int(input())
array = list(map(int,input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])



