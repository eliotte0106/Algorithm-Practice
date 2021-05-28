'''
There are N number of soldiers and each of them has different power.
Front soldier always have more power than the soldier positioned back.
Find counts of removable soldiers in this case.
ex)
1/2/3/4/5/6/7
15/11/4/8/5/2/4
we should remove 3 and 6, so the output should be 2.
'''

n = int(input())
array = list(map(int,input().split()))
array.reverse()

dp = [1] * n

#Using LIS (Longest Increasing Subsequence)
for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))