
import random

def get_choices():

    playa_choice = input( "enter a choice (rock, paper, scissors:)")
    option = ["rock","paper","scissor"]
    computer_choice = random.choices(option)

    choices = {"player":playa_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print("you chose  ", player,"  computer chose ",computer)
    print(f"you chose{player}   and computer computer chose {computer}")
    if player == computer:
     return "it's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"
    elif player == "rock " and computer == "scissors":
        return "paper cover's rock!  you lose"
    elif player == "paper " and computer == "rock":
        return "paper cover's rock!  you win"

    else:
        return "scissors cuts paper! you lose"















choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)

choices  = get_choices()

print(choices)

# dictionary in python is like storing multleple variable at one
# name is the key and beau is the value,
#color is the name and blue is the value
#dict = {"name":"beau","color":"blue"}

