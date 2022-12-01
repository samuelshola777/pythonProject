

num1 = int (input("enter a number to find the maximum and the minimum"))
num2 = int (input("enter a number to find the maximum and the minimum"))
num3 = int (input("enter a number to find the maximum and the minimum"))

maximum = num1
minimum = num1

if num2 > maximum:
     maximum = num2

if num2 < minimum:
     minimum = num2

if num3 > maximum:
     maximum = num3

if num3 < minimum:
     minimum = num3



print(minimum)
print(maximum)
print("<---------------------------------------------------------------------->")
print("after comparining the three value",int(maximum), " is the maximum value ")
print("<----------------------------------------------------------------->")
print("after comparining the three value",int(minimum), " is the minimum value ")