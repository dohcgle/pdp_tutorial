number = int(input("Sonni kiriting: "))

if (number % 3 == 0) and (number % 5) == 0:
    print("FizBiz")
elif number % 3 == 0:
    print("Fiz")
elif number % 5 == 0:
    print("Biz")
else:
    print(number)

