'''
sort numbers reversed
'''
n = int(input())
array = []
for i in range(n):
    num = int(input())
    array.append(num)

array.sort(reverse=True)
for i in array:
    print(i,end= ' ')