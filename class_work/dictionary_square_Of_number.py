dic_number = {
     'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 9,
    'key5': 5

}

for by in  dic_number.keys():
    print(by, ":", dic_number.get(by) * dic_number.get(by))
