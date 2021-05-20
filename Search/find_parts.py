'''
print yes or no if the part is in the list or not.
'''
def binary_search_iterative(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        #if target, return mid
        if array[mid] == target:
            return mid
        #if target is smaller than mid
        elif array[mid] > target:
            end = mid - 1
        #if target is larger than mid
        else:
            start = mid + 1
    return None

n = int(input())
parts = list(map(int,input().split()))

m = int(input())
part = list(map(int,input().split()))

for item in part:
    result = binary_search_iterative(parts,item,0,n-1)
    if result != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")
