import self


class Account_class:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


    def set_name(self, name):
        self.name = name

    def set_balance(self,balance):

         self.balance = balance



    def get_name(self):

        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance