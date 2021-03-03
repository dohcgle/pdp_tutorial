names = input("Ismlarni vergul bilan ajratib kiriting: ").split(",")

def FindMaxLength(names):
    return max(names, key=len)

print(FindMaxLength(names))
