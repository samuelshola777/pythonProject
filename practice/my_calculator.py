if __name__ == '__main__':
    road = 0
    while road == 0:
        operation = int(input("<---->  hi  <--->\n\n welcome to my  calculator \n\n"
                              "for ADDITION PRESS 1\n"
                              "<-------------------->\n"
                              "FOR SUBTRACTION PRESS 2\n"
                              "<---------------------->\n"
                              "FOR MULTIPLICATION PRESS 3\n"
                              "<------------------------->\n"
                              "FOR DIVISION PRESS  4\n  "
                              "<--------------------->\n"
                              "FOR  FOR RAISE TO THE POWER OF PRESS 5\n"
                              "<------------------------------------->\n"
                              "TO CHECK FOR THE REMAINDER OF A PARTICULAR DIVISION REMAINDER\n"
                              "press 6\n\n"
                              "<---->PRESS 900 TO EXIT THE CALCULATOR<----->".upper()))

        if operation == 1:
            num1 = int(input("enter  your first number"))
            num2 = int(input("enter  your second number"))
            sum1 = num1 + num2
            print("*********************your total addition is  ".upper(), sum1)
            operation = input("<-->press 700 to GO BACK TO THE MAIN MENU<--->\n\n"
                              "<--->press 900 to exit the calculator<--->".upper())

        elif operation == 2:
            num1 = int(input("enter  your first number"))
            num2 = int(input("enter  your second number"))
            sum1 = num1 - num2
            print("###############your total addition is  ".upper(), sum1)
            operation = input("<-->press 700 to GO BACK TO THE MAIN MENU<--->\n\n"
                              "<--->press 900 to exit the calculator<--->".upper())

        elif operation == 3:
            num1 = int(input("enter  your first number"))
            num2 = int(input("enter  your second number"))
            sum1 = num1 * num2
            print("$$$$$$$$$$$$$$your total addition is  ".upper(), sum1)
            operation = input("<-->press 700 to GO BACK TO THE MAIN MENU<--->\n\n"
                              "<--->press 900 to exit the calculator".upper())

        elif operation == 4:
            num1 = int(input("enter  your first number"))
            num2 = int(input("enter  your second number"))
            sum1 = num1 / num2
            print("###################your total addition is  ".upper(), abs(sum1))
            operation = input("<-->press 700 to GO BACK TO THE MAIN MENU<--->\n\n"
                              "<--->press 900 to exit the calculator<--->".upper())

        elif operation == 5:
            num1 = int(input("enter  your first number"))
            num2 = int(input("enter  your second number"))
            sum1 = num1 ** num2
            print("@@@@@@@@@@@@@@@@@your total addition is  ".upper(), sum1)
            operation = input("<-->press 700 to GO BACK TO THE MAIN MENU<--->\n\n"
                              "<--->press 900 to exit the calculator<--->".upper())

        elif operation == 6:
            num1 = int(input("enter  your first number"))
            num2 = int(input("enter  your second number"))
            sum1 = num1 % num2
            print("****************your total addition is  ".upper(), sum1)
            operation = int(input("<-->press 700 to GO BACK TO THE MAIN MENU<--->\n\n"
                              "<--->press 900 to exit the calculator<--->".upper()))


        elif operation == 700:
            continue
        elif operation == 900:
            break
        else:  print("<-----you hae entered an invalid option---->".upper())


