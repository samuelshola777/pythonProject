count = 0

arrayNumber = []
while count < 3:
    num = int(input("please enter number 1 and 2 only"))
    if num != 1 and num != 2:
        continue
    arrayNumber.append(num)
    count = +1
    if count == 3:
        break
