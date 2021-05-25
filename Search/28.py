'''
Find a fixed point, which means that the value and the index are same.
Return the fixed point, otherwise, if there is no fixed point, return -1.
For ex)
-15 -6 1 3 7 shoud return 3
'''

def binary_serach(array,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    while start < end:
        if mid == array[mid]:
            return mid
        elif mid < array[mid]:
            return binary_serach(array,start,mid-1)
        else:
            return binary_serach(array,mid+1,end)
    

n = int(input())
nums = list(map(int,input().split()))
index = binary_serach(nums, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)