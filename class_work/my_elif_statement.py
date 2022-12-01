def name_of_function():







    counter = 0

    while counter != 5:
        result = int(input("please enter grade: "))

        if 100 >= result >= 90:
            print("your grade is A")
        elif 89 >= result >= 70:
            print("your total grade is B")
        elif 50 <= result <= 69:
            print(" your total grade is C")
        elif 49 >= result >= 40:
            print("your total grade is D")
        elif 39 >= result >= 30:
            print("your total grade is E")
        elif 0 < result < 30:
            print("you have zero talent")
        else:
            print("Grade invalid")

        counter += 1

        if counter == 5:
            print("No available moves")
            break

if __name__ == '__main__':

    name_of_function()