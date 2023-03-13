class Petrol_Purchase:
    def __init__(self):
        self.station_location = None
        self.petrol_type = None
        self.price_per_liter = None
        self.liter_purchased = 0
        self.discount_per_liter = 0.0

    def set_station_location(self, station_location):
        self.station_location = station_location

    def set_petrol_type(self, petrol_type):
        self.petrol_type = petrol_type

    def set_price_per_liter(self, price_per_liter):
        self.price_per_liter = price_per_liter

    def set_liter_purchased(self, bought_liter):
        self.liter_purchased = bought_liter

    def set_discount_per_liter(self, discount_Amount):
        self.discount_per_liter = discount_Amount

    def get_purchased_amount(self):
        total_petrol_amount = self.liter_purchased * self.price_per_liter - self.discount_per_liter
        return total_petrol_amount


if __name__ == '__main__':
    petrol_purchase = Petrol_Purchase()
    
