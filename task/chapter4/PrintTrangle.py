def printTrangle(number_of_trangles):
    for i in range(number_of_trangles):
        for j in range(i):
            print("*", end=" ")
        print()


if __name__ == '__main__':
    while True:
        number = int(input("enter number of star "))

        printTrangle(number)
    #
    # control = string(input("press yes to continue or press anything to stop"))
    # if control == "yes":
