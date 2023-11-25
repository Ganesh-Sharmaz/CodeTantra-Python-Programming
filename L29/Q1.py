import math
num = float(input(“num: "))
if (num - int(num) >= 0.5):
    print ("result:",math.ceil(num) ) #print the ceil value of num
else:
    print(“result:",math.trunc(num) ) #print the trunc value of num
