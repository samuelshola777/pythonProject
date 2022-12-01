num1 = int(input("please your first input"))
num2 = int(input("please your second input"))

first_num = num1 ** num1 ** num1
second_num = num2 ** num2

if first_num % second_num == 0:
    print("it's a multiple")
else:
    print("it's not a multiple")


