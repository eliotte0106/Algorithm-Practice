#Find minimum counts to make all 0's or 1's when 0 or 1 are consecutive
#ex 0001100 -> only 1 time because 11 to 00 -> 0000000

data = input()

count0 = 0
count1 = 0

if data[0] == '1':
    count0 +=1
else:
    count1 +=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 +=1
        else:
            count1 +=1
print(min(count0,count1))
