"""
make 1 using 4 rules (Find minimum count of calls to make 1).
a)if x divides by 5, divide by 5
b)if x divides by 3, divide by 3
c)if x divides by 2, divide by 2
d) else, -1
"""
#a_i = min(a_(i-1),a_(i/2),a_(i/3),a_(i/5))+1

#DP bottom-up
x = 26
d = [0] * 30001

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)
print(d[x])