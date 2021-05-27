'''
From the given triangle, you should choose 1 number at each level.
You can choose the number positioned on the left-unde or the right-under.
Find the biggest sum of this triangle.
ex)
                7
            3       8
        8       1       0
    2       7       4       4
4       5       2       6       5

output: 30 ( 7 + 3 + 8 + 7 + 5)

'''

n = int(input()) # size of triangle
dp = []
for i in range(n):
    nums = list(map(int,input().split()))
    dp.append(nums)

for i in range(1,n):
    for j in range(i+1):
        #up left
        if j == 0: # if [i][0], there is no left element
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        #up    
        if j == i:# if so, there is no right element 
            up = 0
        else:
            up = dp[i-1][j]
        #max sum stored
        dp[i][j] = dp[i][j] + max(up,up_left)

#print max number from the row
print(max(dp[n-1]))