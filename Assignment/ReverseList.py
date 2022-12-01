sam_list = [6, 7, 90, 45, 23, 12]
reverse_list = []
for i in range(len(sam_list)):
    reverse_list += [sam_list[len(sam_list) - 1 - i]]

print(reverse_list)