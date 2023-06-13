array = [1, 2, 3, 4, 5,16, 71, 8, 9, 10]
largest = 0;
secondLargest = 0;

for i in range(len(array)):
    if array[i] > largest:
        largest = array[i]

print(largest)

for i in range(len(array)):
    if array[i] > secondLargest and array[i] != largest:
        secondLargest = array[i]
print("()->  ", secondLargest)
