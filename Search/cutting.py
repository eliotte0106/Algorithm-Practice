'''
find the maximum height to give at least M length woods

ex)
There are 19, 15, 10, 17 height woods and the customer wants the wood that has the height of at least 6.
Then you shoud use 15 height cutter since, after cutting, 4,0,0,2 will be left that gives total 6
'''

n, m = map(int, input().split())
woods = list(map(int,input().split()))

start = 0
end = max(woods)

#binary_search

result = 0
while start <= end :
    total = 0
    mid = (start + end) // 2
    #after cut
    for x in woods:
        if x > mid :
            total += x - mid
    #if the length of wood is not satisfied, cut more(search left side)
    if total < m :
        end = mid - 1
    #if the length of wood is enough, cut less(search right side)
    else:
        result = mid
        start = mid + 1

print(result)