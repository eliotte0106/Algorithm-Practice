"""
n x m sized gold.
can start from the first column and any row.
At each step, keep find the biggest number in the column
3 choices: right upper, right, right under
find the maximum gold sum.

ex:
 3x3

1|2|3
ㅡㅡㅡㅡ
4|5|6
ㅡㅡㅡㅡ
7|8|9

best result should be 7 + 8 + 9 = 24
"""
#dp[i][j] = array[i][j]+max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])

tc = int(input())
for i in range(tc):
    n, m = map(int,input().split())
    gold = list(map(int,input().split()))

dp = []
index  = 0
for i in range(n):
    dp.append(gold[index:index+m])
    index += m

for j in range(1,m):
    for i in range(n):
        if i == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
        if i == n-1:
            left_down = 0
        else:
            left_down = dp[i+1][j-1]
        left = dp[i][j-1]
        dp[i][j] = dp[i][j]+max(left_up,left_down,left)

result = 0
for i in range(n):
    result = max(result,(dp[i][m-1]))

print(result)


