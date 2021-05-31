'''
1. insert ( only one character)
2. remove ( " )
3. replace ( " )
Count how many operators would be used to change from A to B
ex)
cat
cut
output : 1

sunday
saturday
output : 3
'''
#first attempt
a = input()
b = input()
l = len(b) - len(a)
count = 0
array = []
array2 = []
for i in range(len(a)):
    array.append(a[i])
for i in range(l):
    array.append(i)

for i in range(len(b)):
    array2.append(b[i])

for x in array:
    if x not in array2:
        count += 1

print(count)

#second attempt (better one)
#dp

def edit_dist(str1,str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0] = i
    for j in range(1,m+1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1,m+1):
            #if character is same
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            #if character is different
            else:
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    
    return dp[n][m]

str1 = input()
str2 = input()
print(edit_dist(str1,str2))