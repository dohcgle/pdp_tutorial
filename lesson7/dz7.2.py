word1 = input("1 so'zni kiriting: ").lower()
word2 = input("2 so'zni kiriting: ").lower()

if sorted(word1) == sorted(word2):
    print('Anagramma')
else:
    print('Anagramma emas')

