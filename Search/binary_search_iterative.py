#O(logN),N is the length of the array
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

array = [1,2,3,4,5,6,7,8,9,10]
print(binary_search_iterative(array,8,0,len(array)-1))