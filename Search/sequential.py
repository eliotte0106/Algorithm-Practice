
#O(N), N is the length of array
def sequential(n,target,array):
    for i in range(n):
        if array[i] == target:
            return i

array = ['a','b','c','d','e']

print(sequential(5,'c',array))