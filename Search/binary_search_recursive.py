def binary_search_recursive(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    #if mid is target
    if array[mid] == target:
        return mid
    #if target is smaller than mid
    elif array[mid] > target:
        return binary_search_recursive(array,target,start,mid-1)
    #if target is larger than mid
    else:
        return binary_search_recursive(array,target,mid+1,end)
    
arr = [1,2,3,4,5,6,7,8,9,10]

print(binary_search_recursive(arr,7,0,len(arr)-1))