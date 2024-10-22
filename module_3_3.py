def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(12, 13 )
print_params(11)
print_params(b=25)
print_params(c = [1,2,3])


values_list = [(1, 2, 3), [7, 8, 9], 'milk']
values_dict = {'a': 3, 'b': 'b', "c": 12.1}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, {1, 2, 3}]
print_params(*values_list_2, 42)
