'''
Upper letters and digits are given,
sort this alphanumerically with the sum of digits.
ex(K1KA5CB7 should output ABCKK13)
'''
#first version
s = input()
result = ''.join(sorted(s))
sum = 0
new_result = list()
for i in range(len(s)):
    if result[i].isalpha():
        new_result.append(result[i])
for i in range(len(s)):
    if result[i].isdigit():
        sum += int(result[i])
newsum = str(sum)
for i in range(len(newsum)):
    new_result.append(newsum[i])
print(new_result)

for i in range(len(new_result)):
    print(new_result[i],end='')

#second version (optimal answer)
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))