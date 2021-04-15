

def recursive(arr,i):
    if i < 0:
        return 0
    else:
        cut = arr[i] + recursive(arr,i-2)
        no = recursive(arr,i-1)
        return max(cut,no)

arr = [1,3,1,5]
i = 3
print(recursive(arr,i))
