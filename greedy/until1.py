'''
An Integer number N should be 1.
You can use 2 operations.
1: N-1
2: N //K (if divisible)
count the number of minimum operations until N becomes 1
'''
#In my opinion,
#first and second version : easy to understand 
#third version: little bit confusing

#first version
n,k = map(int,input().split())

cnt = 0
while True:
    if n % k == 0:
        n //= k
        cnt += 1
        if n == 1:
            break
    else:
        n -= 1
        cnt += 1
        if n == 1:
            break
print(cnt)

#second version
n,k = map(int,input().split())
cnt = 0

while n >= k :
    while n % k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1
while n > 1:
    n -= 1
    cnt += 1

print(cnt)

#third version
n, k = map(int,input().split())
cnt = 0

while True:
    target = (n//k)*k
    cnt += n - target
    n = target
    if n < k:
        break
    cnt += 1
    n //= k
cnt += n - 1
print(cnt)