def count(array):
    arr = [0] * (max(array) + 1)

    for i in range(len(array)):
        arr[array[i]] += 1

    for i in range(len(arr)):
        for j in range(arr[i]):
            print(i, end = " ")
        
array = [9,8,7,6,5,4,3,2,1,0]
count(array)