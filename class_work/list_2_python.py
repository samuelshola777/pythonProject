# samuel_shola = {
#     10: 'Ten',
#     20: 'Twenty',
#     30: 'Thirty',
#     40: 'Forty',
#     50: 'Fifty',
#     60: 'Sixty',
#     70: 'Seventy',
#     80: 'Eighty',
#     90: 'Ninty',
#     100: 'Hundred'
# }
#
# my_empty_dictionary = {}
#
# for by in (len(samuel_shola)):
#  my_empty_dictionary = samuel_shola.get(by);
#  print(my_empty_dictionary.get(by))

list_values = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
list_key = [10, 20, 30, 40,  50, 60, 70, 80, 90, 100]

dictionary = {}

values = 0
for i in list_key:
    dictionary[i] = list_values[values]
    values += 1

print(dictionary)