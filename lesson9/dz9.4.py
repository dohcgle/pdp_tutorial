
# numbers = input("Sonlarni vergul bilan ajratib kiriting: ").split(",")
numbers = ["121", "72", "456", "543", "394"]
length = len(numbers)

def reverseWord(word):
    return word[::-1]

for i in range(length):
    item = numbers[length-i-1]
    print(reverseWord(item))
