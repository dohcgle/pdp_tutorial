
my_list = [25,92, 19, 4, -6]
my_dict = {'first_name': 'Ulugbek', 'last_name': 'Taylakov', 'phone': '998909710111'}
num = 21
char = '20'
try:
    print(my_list[8])
    print(my_dict['age'])
    print(num+char)
except IndexError:
    raise IndexError from None
    print(e)
except KeyError:
    print(KeyError)
