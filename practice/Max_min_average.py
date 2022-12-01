grade1=int (input("please enter first grade"))
print("<------------------------------------------>")
grade2=int (input("please enter second grade"))
print("<------------------------------------------>")
grade3=int (input("please enter third grade"))
maximum = grade1
minimum = grade1
if grade2 > maximum:
    maximum = grade2
if grade2 < minimum:
        minimum = grade2
if grade3 > maximum:
      maximum = grade3
if grade3 < minimum:
    minimum = grade3
    print("<------------------------------------------>")
    print("your maximum value is : ",maximum)
    print("<------------------------------------------>")
    print("your minimum value is : ",minimum)
    average = grade1 + grade2 + grade3
    averagen = average // 3
    print("<------------------------------------------>")
    print("and the average grade is :",averagen)
for i in range(1,12):
       print('*'*i)
for z in range(1,12,-1):
       print('*'*z)