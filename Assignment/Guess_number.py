if __name__=='__main__':


    def guess_number(number):
        import random

        random_number = random.randint(1,1000)
        print("my name is samue shola")
        print("<<---------------------------------------------------->>")
        print()
        if number != random_number and number > random_number:
            print("your guess is too high please try again")
        if number != random_number and number < random_number:
            print("your guess is too low, please try again")
        if number == random_number:
            print("yes, you made it now you \n"
                  " can have the hand of my teacher in marriage")
        print("<<---------------------------------------------------->>")
        print( "the altimate ********    ",random_number)


number  =int (input("please name by force to guess") )

guess_number(number)
