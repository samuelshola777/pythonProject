class Item:
    # contructor
    def __init__(self, name):
        self.name = "boneshaker"
        self.price = 100
        self.quantity = 5
        print(f"An instance created: {name}")

    def calculate_total_amount(self, quantity, price) -> int:
        return price * quantity


item1 = Item("boneshaker")
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_amount(item1.price, item1.quantity))

item2 = Item("sales")
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_amount(item2.price, item1.quantity), "   my name is samuel shola")
