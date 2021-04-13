#n = # of number, m = # of total calculation, k = # of calculation of big num
n,m,k = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
first = num[len(num)-1]
second = num[len(num)-2]
sum = 0

#my first version
# for i in range(0,m):
#     sum += first * k
#     m -= k
#     if m == 0:
#         break
#     sum += second
#     m -= 1
#     if m == 0 :
#         break

#second version
while True:
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1
    
    if m == 0:
        break
    sum += second
    m -= 1
    
print(sum)