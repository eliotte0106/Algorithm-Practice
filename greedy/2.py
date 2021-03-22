#find the biggest result using + and *
data = input()

big_num = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or big_num <=1:
        big_num += num
    else:
        big_num *= num

print(big_num)
