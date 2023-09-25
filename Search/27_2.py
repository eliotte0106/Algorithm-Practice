'''
count how many x is in the list. The runtime should be O(logN).
ex)
[1,1,2,2,2,2,3]
should output 4
solution: last index of 2 - first index of 2 will be the answer using binary search
'''

from bisect import bisect_left, bisect_right

def count_by_range(array,left_value,right_value):
    right_index = bisect_right(array,right_value) #idx 5 -> this idx is last idx of 2 + 1
    left_index = bisect_left(array,left_value) #idx 2
    return right_index - left_index

n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_range(array,x,x)

if count == 0:
    print(-1)

else:
    print(count)
