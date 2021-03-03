import math
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

d = b*b - 4*a*c

if d == 0:
    print("Tenglama 1 ta yechimga ega")
elif d < 0:
    print("Tenglama 0 ta yechimga ega")
elif d > 0:
    print("Tenglama 2 ta yechimga ega")
