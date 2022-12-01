import random

# random.seed(4)
# print(random.randint(1,10))


times = 0

while times <= 10:
    times += 1

    guess = int(input("try to guess the hiden number"))

    numbers = random.randint(1, 10)
    print("<--------------------------------------------->")
    print("the ultimate guess is", numbers)
    print("<--------------------------------------------->")
    if guess == numbers:
        print("you guessed right")
    elif guess < numbers:
        print("nah your guess is lower the  the ultimate number")
    elif guess > numbers:
        print("your guess is atuall higer than the ultimate number")
        if times == 7:
            print("you have three more try")
            continue
        if times == 10:
            print("game over".upper())
            break
