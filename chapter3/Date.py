class Date:
    def __init__(self, date, month, year):
        self.date = 0
        self.month = 0
        self.year = 0

    def set_date(self, date):
        if date < 32:
            self.date = date

    def set_month(self, month):
        if month < 12:
            self.month = month

    def self_year(self, year):
        self.year = year

    def get_year(self):
        return self.year


if __name__ == '__main__':
    me_Date = Date(12, 4, 1996)

    me_Date.self_year(1970)

    print(" this is the year you're talking about   ",me_Date.get_year())
