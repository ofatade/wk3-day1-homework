# Task 1: Formatting Flight Itineraries

atuple = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Dare", "Atlanta", "Lagos")]

def itinerary(atuple):
    for index, (traveler_name, origin, destination) in enumerate(atuple, start=1):
        print(f"Itinerary {index}: {traveler_name} - From {origin} to {destination}")

itinerary(atuple)