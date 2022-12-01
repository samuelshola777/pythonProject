if __name__=='__main__':

    number = int(input("please input a number: "))
    total = 0
    for i in range(1, number+1):
        if number % i == 0:
            total = total + i
            print(i)

    print(total)

    if total == number:
         print("it's a perfect number")
    else: print("it's not a perfect number")