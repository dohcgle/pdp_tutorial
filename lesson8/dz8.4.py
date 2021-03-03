names = input("Ismlarni vergul bilan ajratib kiriting: ").split(",")

def FindMinLength(names):
    return min(names, key=len)

print(FindMinLength(names))

