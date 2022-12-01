
my_set = set()

counter = 0
while counter < 5:
    try:
        collect_number = int(input("please input number from 2 to 90 five times \n"))

        if 2 <= collect_number <= 90:
            collect_number = my_set.add(collect_number)
            print("Number saved")
        else:
            print("you entered an invalid number ")
            continue
    except ValueError as samuelShola:
        print(samuelShola)

    if len(my_set) == 5:
        break
print(my_set)
