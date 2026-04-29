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

    def _validate(self, distance_m: int, speed_kmh: float, elapsed_sec: int) -> None:
        if not isinstance(distance_m, int):
            raise TypeError(f"distance_m must be an int: {distance_m!r}")
        if distance_m < 0:
            raise ValueError(f"distance_m must be non-negative: {distance_m}")
        if speed_kmh < 0:
            raise ValueError(f"speed_kmh must be non-negative: {speed_kmh}")
        if not isinstance(elapsed_sec, int):
            raise TypeError(f"elapsed_sec must be an int: {elapsed_sec!r}")
        if elapsed_sec < 0:
            raise ValueError(f"elapsed_sec must be non-negative: {elapsed_sec}")

    def update(self, distance_m: int, speed_kmh: float, elapsed_sec: int) -> None:
        self._validate(distance_m, speed_kmh, elapsed_sec)
        self._update_distance_fare(distance_m)
        self._update_time_fare(speed_kmh, elapsed_sec)
