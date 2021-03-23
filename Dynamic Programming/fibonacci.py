"""
fibonacci

a_(n+2) = f(a_(n+1),a_n) = a_(n+1) + a_n
a_n = a_(n-1) + a(n_2)

"""
#1. Using recursion

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(6)) # 1,1,2,3,5,8

#this recursion takes too much time. -> bad solution, O(2^N)



#2. Using memoization = caching

#list
d = [0] * 100

#recusive implementation using top-down DP
def fibo2(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]

print(fibo2(6))

#momerizes visited nodes and calls them. O(N), f(1)->f(2)->f(3)

#checking which function is called

d2 = [0] * 100

def pibo(x):
    print('f(' +str(x)+ ')' ,end = " ")
    if x == 1 or x == 2:
        return 1
    if d2[x] != 0:
        return d[x]
    d2[x] = pibo(x-1) + pibo(x-2)
    return d2[x]

pibo(6)

"""
To solve a big proglem, calling small problems is called "Top-Down".
However, using for loop to solve a problem is called "Bottom-Up".

"""

#For loop (Bottom-Up)
print("")
d3 = [0] * 100
def fibo3(n):
    d3[1] = 1
    d3[2] = 1
    
    for i in range(3,n+1):
        d3[i] = d3[i-1] + d3[i-2]
    return d3[i]

print(fibo3(6))
