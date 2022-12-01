num1 = int(input("please enter your first integer"))
num2 = int(input("please enter your first integer"))
num3 = int(input("please enter your first integer"))

add = num1 + num2 + num3


print("the total value of the inputed value is ",add)


average = num1 + num2 + num3 // 3

minimum = num1
maximum = num1

if num2 > maximum:
    maximum = num2

if num2 < minimum:
    minimum = num2

if num3 > maximum:
    maximum = num3

if num3 < minimum:
    minimum = num3

    print(" the maximum value of the three input is ", maximum)

    print(" the minimum value of the three input is ", minimum)

    product = num1 * num2 * num3
    print("the product of the three input value is ",product)

