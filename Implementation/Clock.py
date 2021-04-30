'''
From the input N,
find the count of number of time that includes 3 from 00:00:00 to N:59:59
'''

n = int(input("Enter the time: "))
count = 0
for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

