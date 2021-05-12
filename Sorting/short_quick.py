#short quick sort using python's advantages

def quick_sort(array):
    #if the list has less than or equal to 1 element
    if len(array) <= 1:
        return array
    
    pivot = array[0] # first element
    tail = array[1:] # remaining element except the first element

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [5,7,6,9,4,2,1,3,0,8]
print("before quick sort:",array)
result = quick_sort(array)
print("after quick sort:",result)