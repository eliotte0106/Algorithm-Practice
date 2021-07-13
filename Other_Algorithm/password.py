'''
Find the possible passwords
Rules)
1. the password is composed of 4 different letters with at least 1 vowel and 2 consonants.
2. the password should be sorted ascendingly. ex (abc, bcd, ...)

'''

from itertools import combinations

vowels = ('a','e','i','o','u')
l,c = map(int,input().split()) # l = length of password, c = num of kinds of alphabet

array = input().split(' ')
array.sort()

for password in combinations(array,l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    
    if count >= 1 and count <= l - 2:
       print(''.join(password))