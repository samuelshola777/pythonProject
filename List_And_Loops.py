num = [6, 3, 2, 4, 90, 11, 45, 4, 7]
# my_list = [n for n in num]
# print(my_list)
# for n in num:
#     my_list.append(n)
# print(my_list)

# printing out the square of num which means number * number
# for n in num:
#     my_list.append(n * n)
# print(my_list)
# my_lists = [n*n for  n in num]
# print(my_lists)
my_list = [lambda n: n * n, num]
print(my_list)
