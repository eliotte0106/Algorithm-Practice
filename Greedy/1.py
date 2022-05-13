
n = int(input()) #input
data = list(map(int,input().split())) # data
data.sort()
group = 0
count = 0
#make a group if count = i (element in data)
for i in data:
    count += 1
    if count >= i :
        group +=1
        count = 0
print(group)
