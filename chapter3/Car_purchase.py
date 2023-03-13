class Car_purchase:
    def __init__(self,):
        self.car_type = None
        self.car_year = None
        self.car_price = 0.0

    def set_car_type(self, car_type):
        self.car_type = car_type

    def set_car_year(self, car_year):
        self.car_year = car_year

    def set_car_price(self, car_price):
        self.car_price = car_price

    def car_Receipt_five_pesent(self, car_type, car_year, car_price):
        discount_added = 0.5
        total_purchase = car_price - 0.5
        return """
        car_type = %s
        car_year = %s
        car_price = %
        """, car_type, car_year, car_price, discount_added, total_purchase

    def car_Receipt_seven_pesent(self, car_type, car_year, car_price):
        discount_added = 0.7
        total_purchase = car_price - 0.7
        return """
        car_type = %s
        car_year = %s
        car_price = %
        """, car_type, car_year, car_price, discount_added, total_purchase


if __name__ == '__main__':
    car1 = Car_purchase()

    # print(car1.car_Receipt_five_pesent('volvo,'2019',2000000000))