'''
There are N x M cards, you should pick the biggest number.
However, you should pick the smallest number in the row.
'''
# In my opinion, it will be easy to pick max(min(nums in rows))

result = 0

n,m = map(int,input().split())
for i in range(n):
    nums = list(map(int,input().split()))
    small = min(nums)
    big = max(small,result)

print(big)
