
"""IndexError"""
my_list = [25,92, 19, 4, -6]
try:
    print(my_list[8])
except IndexError as e:
    print(e)

"""KeyError"""
my_dict = {'first_name': 'Ulugbek', 'last_name': 'Taylakov', 'phone': '998909710111'}
try:
    print(my_dict['age'])
except KeyError as e:
    print(e)