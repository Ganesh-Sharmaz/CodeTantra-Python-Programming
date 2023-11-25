#write your code here
n = int(input('n: '))
row = 1
value = 1
while row <= n:
    col = 1
    while col <= row:
        print(value, end = * ')
        value += 1
        col += 1
    row += 1
    print()
