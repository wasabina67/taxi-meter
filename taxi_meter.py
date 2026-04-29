class TaxiMeter:

    def __init__(self):
        base_fare = 500

        self.total_distance = 0.0
        self.total_time_low_speed = 0
        self.fare = base_fare

    def update(self):
        return

    def get_fare(self):
        return self.fare
