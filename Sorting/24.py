'''
find the house that is connected to other houses with minimum distance
'''

n = int(input())

house = list(map(int,input().split()))
house.sort()

#median position finds the house with minimum distance from other houses
print(house[(n-1)//2])