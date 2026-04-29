class TaxiMeter:

    BASE_FARE = 500

    def __init__(self):
        self.reset()

    def reset(self):
        self.total_distance = 0.0
        self.total_time_low_speed = 0
        self.fare = self.BASE_FARE

    def _update_time_fare(self, speed_kmh, elapsed_sec):
        low_speed_threshold = 10
        time_step = 90
        time_fare = 100

        if speed_kmh <= low_speed_threshold:
            prev_time = self.total_time_low_speed
            self.total_time_low_speed += elapsed_sec

            added_steps = int(self.total_time_low_speed / time_step) - int(prev_time / time_step)
            self.fare += added_steps * time_fare

    def _update_distance_fare(self, distance_km):
        base_distance = 1.0
        distance_step = 0.3
        distance_fare = 100

        prev_distance = self.total_distance
        self.total_distance += distance_km

        if self.total_distance > base_distance:
            extra_distance = self.total_distance - base_distance
            prev_extra_distance = max(0, prev_distance - base_distance)

            added_steps = int(extra_distance / distance_step) - int(prev_extra_distance / distance_step)
            self.fare += added_steps * distance_fare

    def update(self, distance_km, speed_kmh, elapsed_sec):
        self._update_distance_fare(distance_km)
        self._update_time_fare(speed_kmh, elapsed_sec)

    def get_fare(self):
        return self.fare
