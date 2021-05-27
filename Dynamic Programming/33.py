'''
After N days, he is planning to retire from his job.
He wants to make best profit before he retires.
ex)
given N = 7,
    1  /  2 /  3  /  4  /  5  / 6  /  7 : 1 to N
    3  /  5 /  1  /  1  /  2  / 4  /  2 : days of work on the given date
    10 / 20 / 10  / 20  / 15 / 40 / 200 : Pay

Best profit: from day 1,4,5, 10 + 20 + 15 = 45
'''

n = int(input())
days = []
pay = []

dp = [0] * (n+1)
max_val = 0

for _ in range(n):
    x,y = map(int,input().split())
    days.append(x)
    pay.append(y)

# from back
for i in range(n-1,-1,-1):
    time = days[i] + i
    #if possible to work
    if time <= n:
        #max value
        dp[i] = max(pay[i]+dp[time],max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)