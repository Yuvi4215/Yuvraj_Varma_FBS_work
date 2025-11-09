class TVException(Exception):
    def validate(self, model, screen, price):
        if model < 1 or model > 9999 or screen < 12 or screen > 70 or price < 0 or price > 5000:
            raise TVException("Invalid Input")