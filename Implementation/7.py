'''
Lucky Straight Problem:
integer N is given ( should be even digit ex(12,1234,123456,...) ),
Halve the N, and if the sum of left side equals to the sum of the right side, print LUKCY, else, print READY
'''

#first version

N = int(input())
num = str(N)
l = len(num)//2
leftsum = 0
rightsum = 0

for i in range(l):
    leftsum += int(num[i])

for i in range(l,len(num)):
    rightsum += int(num[i])

if leftsum == rightsum:
    print("LUCKY")
else:
    print("READY")

#second version (optimal answer)

N = input()
length = len(N)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2,length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
