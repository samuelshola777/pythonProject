grade1 = int(input("please enter first grade"))
print("<--------------------------------------->")
grade2 = int(input("please enter second grade"))
print("<--------------------------------------->")
grade3 = int(input("please enter third grade"))

maximum = grade1


if grade2 > maximum:
    maximum = grade2

if grade3 > maximum:
    maximum = grade3

minimum = grade1
if grade2 < minimum:
    minimum = grade2

if grade3 < minimum:
    minimum = grade3

print("your maximum value is : ", maximum)
print("your minimum value is :", minimum)
