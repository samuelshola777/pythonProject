def multiplication_table(number):
    table = int(input("please input value: "))
    print("time    table      result")
    for time in range(1, 13, 1):

        mulple = time * table;

        print(time,"  *    ",table," =      ",mulple)

if __name__ == '__main__':
    multiplication_table()

