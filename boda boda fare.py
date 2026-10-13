class BodaBoda:
    def __init__(self, name, destination, distance, Basefare=2000, fare_per_kilometre=1000):
        self.client = name
        self.destination = destination
        self.distance = distance
        self._Basefare = Basefare
        self._fare_per_kilometre = fare_per_kilometre

    def get_Basefare(self):
        return self._Basefare

    def get_Distancefare(self):
        return self.distance * self._fare_per_kilometre

    def get_total_fare(self):
        return self.get_Basefare() + self.get_Distancefare()


journeys = [
    BodaBoda("Jermimah", "Entebbe", 8),
    BodaBoda("Kenneth", "Jinja", 10),
    BodaBoda("Aisha", "Mukono", 12),
]

for journey in journeys:
    print(f"{journey.client}: Kampala to {journey.destination}")
    print(f"Distance: {journey.distance} km")
    print(f"Base fare: UGX {journey.get_Basefare():,}")
    print(f"Distance fare: UGX {journey.get_Distancefare():,}")
    print(f"Total fare: UGX {journey.get_total_fare():,}\n")