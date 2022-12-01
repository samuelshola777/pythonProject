if __name__ == '__main__':
    number = int(input("Enter a value: "))
    total = 0
    print("The factor are: ", end=' ')
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=' ')
        total = total + 1
    print("\nSum of factors is: ", total)

