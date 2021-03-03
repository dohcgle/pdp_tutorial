# words = ['alice', 'john', 'bob', 'alice', 'john', 'alice']
# maqsad = 'alice'

words = input("Vergul bilan ajaratib so'zlar kiriting: ").split(sep=",")
maqsad = input("Maqsad so'zni kiriting: ")

result = words.count(maqsad)

print(result)