from taxi_meter import TaxiMeter

def main():
    meter = TaxiMeter()

    trips = [
        {"distance_m": 500, "speed_kmh": 30.0, "elapsed_sec": 60},
        {"distance_m": 300, "speed_kmh": 5.0, "elapsed_sec": 90},
        {"distance_m": 100, "speed_kmh": 3.0, "elapsed_sec": 120},
        {"distance_m": 400, "speed_kmh": 40.0, "elapsed_sec": 40},
    ]

    for i, t in enumerate(trips, 1):
        meter.update(t["distance_m"], t["speed_kmh"], t["elapsed_sec"])
        print(f"Trip {i}: {meter.get_fare()}")


if __name__ == "__main__":
    main()
