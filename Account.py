from class_work.my_firstclass import Account_class

if __name__ == '__main__':

    result = Account_class("my name is samuel shola", 16, 0.0)
    print(result.get_name())

    change_name = input('please inputyour neew accout name: ')

    result.set_name(change_name)

    print("my name is: "+result.get_name())

    print("your account balance is",result.get_balance())