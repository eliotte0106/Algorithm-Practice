'''
print yes or no if the part is in the list or not.
'''

#using set

n = int(input())

#either list or set works fine
#parts = list(map(int,input().split()))
parts = set(map(int,input().split()))

m = int(input())
part = list(map(int,input().split()))

for item in part:
    if item in parts:
        print("yes", end = " ")
    else:
        print("no", end = " ")