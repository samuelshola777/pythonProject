numb = [4, 5, 6, 700, 80, 9, 10, 110, 19]
firstLargest = numb[0]
secondLargest = 0

for i in range(len(numb)):
    if numb[i] > firstLargest:
        firstLargest = numb[i]

for i in range(len(numb)):
    if numb[i] > secondLargest and numb[i] != firstLargest:
        secondLargest = numb[i]
print(firstLargest)

print(secondLargest, end="  second")
