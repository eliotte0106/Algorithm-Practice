'''
For the given money, find the minimum number of count of elements to make a given money.
If you cannot make it, return -1
ex)
elements: 2, 3, 5
the given money : 7
you should return 2 ( 2 + 5 )
'''

n, m = map(int,input().split()) # n = num of elements, m = target
array = []
for i in range(n):
    array.append(int(input()))

#dp table
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j],d[j-array[i]]+1)
if d[m] != 10001:
    print(d[m])
else:
    print(-1)
