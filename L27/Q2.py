#write your code here
n = int(input('n: '))
l = len(str(n))
Summ = 0
a=n
while n > 0:
    temp = n % 10
    n=n//10
    summ += temp ** 1
print('sum of powers: ', summ)
if summ == a:
    print(“armstrong number”)
else:
    print("not armstrong number”)
