import math

print("degrees 0 30 45 60 90")

#convert the given degrees to radians

angles = [0,30,45,60,90]

#print the trigoometric values of the radians for sin, cos, tan

print("sin " + " ".join(f"{math.sin(math.radians(angle))}" for angle in angles))
print("cos " + " ".join(f"{math.cos(math.radians(angle))}" for angle in angles))
print("tan " + " ".join(f"{math.tan(math.radians(angle))}" for angle in angles))
