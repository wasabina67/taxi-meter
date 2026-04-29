class TaxiMeter:

    BASE_FARE = 500

    def __init__(self):
        self.reset()

    def reset(self):
        self.total_distance = 0
        self.total_time_low_speed = 0
        self.fare = self.BASE_FARE

    def get_fare(self) -> int:
        return self.fare

    def _update_time_fare(self, speed_kmh: float, elapsed_sec: int) -> None:
        low_speed_threshold = 10
        time_step = 90
        time_fare = 100

        if speed_kmh <= low_speed_threshold:
            prev_time = self.total_time_low_speed
            self.total_time_low_speed += elapsed_sec

            added_steps = self.total_time_low_speed // time_step - prev_time // time_step
            self.fare += added_steps * time_fare

    def _update_distance_fare(self, distance_m: int) -> None:
        base_distance = 1000
        distance_step = 300
        distance_fare = 100

        prev_distance = self.total_distance
        self.total_distance += distance_m

        if self.total_distance > base_distance:
            extra_distance = self.total_distance - base_distance
            prev_extra_distance = max(0, prev_distance - base_distance)

            added_steps = extra_distance // distance_step - prev_extra_distance // distance_step
            self.fare += added_steps * distance_fare

    def update(self, distance_m: int, speed_kmh: float, elapsed_sec: int) -> None:
        self._update_distance_fare(distance_m)
        self._update_time_fare(speed_kmh, elapsed_sec)
