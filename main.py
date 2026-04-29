from taxi_meter import TaxiMeter

def main():
    meter = TaxiMeter()

    trips = [
        {"distance_km": 0.5, "speed_kmh": 30, "elapsed_sec": 60},
        {"distance_km": 0.3, "speed_kmh": 5, "elapsed_sec": 90},
        {"distance_km": 0.1, "speed_kmh": 3, "elapsed_sec": 120},
        {"distance_km": 0.4, "speed_kmh": 40, "elapsed_sec": 40},
    ]

    for i, t in enumerate(trips, 1):
        meter.update(t["distance_km"], t["speed_kmh"], t["elapsed_sec"])
        print(f"Trip {i}: {meter.get_fare()}")


if __name__ == "__main__":
    main()
