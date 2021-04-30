'''
8 X 8 chess board, rows(1~8), columns(a~h).
From the given position, count the number of possible moves of knight.
ex)a1 should output 2
'''

data = input()
row = int(data[1])
#The ord() function returns an integer representing the Unicode character
column = int(ord(data[0]))-int(ord('a'))+1

steps=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
count = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row < 9 and next_column >= 1 and next_column < 9:
        count += 1
print(count)