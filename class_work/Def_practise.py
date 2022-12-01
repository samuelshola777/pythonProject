# pizz_price = 7200
# current_amount = 4300
#
# sleeping_offence = int(input("please enter amount"))
# what_app_offence = 200


def sleep(pizza_price, current_amount, sleeping_offence):
    difference = (pizza_price - current_amount) / sleeping_offence

    print(int(difference))

def what_appoffence(pizza_price, current_amount, web_offence):
    difference = (pizza_price - current_amount) / web_offence
    print(int(difference))

if __name__ == '__main__':
    sleeping_offence = int(input("please enter sleeping_offence amount: "))
    current_amount = int(input("please enter current_amount amount: "))
    pizza_price = int(input("please enter pizza_price amount: "))
    sleep(pizza_price, current_amount, sleeping_offence)

    
    what_appoffence = int(input("please enter sleeping_offence amount: "))
    current_amount = int(input("please enter current_amount amount: "))
    pizza_price = int(input("please enter pizza_price amount: "))
    what_appoffence(pizza_price, current_amount, what_appoffence())
