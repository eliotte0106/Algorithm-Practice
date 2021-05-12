#quick sort
#formal way

def quick_sort(array,start,end):
    #if there is nothing to sort
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]: #from left to right, until finds a larger number, +1
            left += 1
        while right > start and array[right] >= array[pivot]: #from right to left, until finds a smaller number, -1
            right -= 1
        if left > right:
            array[right],array[pivot] = array[pivot],array[right] # if left and right crosses
        else:
            array[left],array[right] = array[right],array[left] # else, just change positions

    #quick sort on the left side and right side
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print("before quick sorting:",array)
quick_sort(array,0,len(array)-1)
print("after quick sorting:", array)


