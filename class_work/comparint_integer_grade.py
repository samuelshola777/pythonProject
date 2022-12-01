
while "true":
    grade = int(input("please enter grade to compare"))

    if grade >= 30:
        print('you entered an invalid grade, \n\nplease enter a valid grade')
        continue
    elif grade < 30:
        break

    if 100 >= grade >= 90:
        print("your total grade is = A")
    elif 89 <= grade >= 70:
        print("your total grade is = B ")
    elif 50 <= grade >= 69:
        print("your total grade is = C")
    elif 40 <= grade >= 49:
        print("your total grade is = D")
