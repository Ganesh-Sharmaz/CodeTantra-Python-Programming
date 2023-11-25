#write your code here
rows = int(input("rows: "))
for index in range(0, rows):
    for spaces in range(rows, index, -1):
        print(" ", end = '')
    number-1
    for col in range(0, index+1):
        print("%d" % number, end=' ')
        number = number* (index-col)/(col+1)
    print()
