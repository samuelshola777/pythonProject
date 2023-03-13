class Clock:
    def __init__(self, hour, minute, seconds):
        self.hour = 0
        if hour > 23:
            hour = 0
        if minute > 59:
            minute = 0
        self.minute = 0
        if seconds > 59:
            seconds = 0
        self.seconds = 0

    def set_hour(self, hour):
        self.hour = 0
        if hour > 23:
            hour = 0

    def set_minute(self, minute):
        if minute > 59:
            minute = 0
        self.minute = 0

    def set_seconds(self, seconds):
        if seconds > 59:
            second = 0
        self.seconds = 0


if __name__ == '__main__':
    time1 = Clock(3, 45, 9)
    print(time1)

