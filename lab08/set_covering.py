def findStations(wanted_cities, stations):
    """
    Finds the minimum set of stations to cover all wanted cities using a greedy algorithm.
    """
    covered_cities = set()
    selected_stations = []

    # Early check: if any wanted city does not appear in any station, no solution exists.
    available_cities = set()
    for city_set in stations.values():
        # Union all cities covered by every station
        available_cities |= city_set
    # Filter out cities that cannot be covered by any station
    wanted_cities &= available_cities

    # Greedy loop: each iteration selects the station covering the most uncovered cities
    while wanted_cities - covered_cities:
        best_station = None
        max_new_cities = 0

        # Cities still not covered in this iteration
        remaining_cities = wanted_cities - covered_cities

        for station_name, city_set in stations.items():
            # Count how many uncovered cities this station can cover
            new_cities = city_set & remaining_cities

            if new_cities:
                num_new = len(new_cities)

                # If it covers more cities, update the best station
                if num_new > max_new_cities:
                    max_new_cities = num_new
                    best_station = station_name

        if not best_station:
            return []  # No solution found

        selected_stations.append(best_station)
        # Mark cities covered by the chosen station as covered
        covered_cities |= stations[best_station]

    return sorted(selected_stations)

def main():
    """Main function to test the set covering problem."""
    stations = {}

    import json

    wanted_cities = json.loads(input())
    station_numbers = int(input())
    # Read each station's name and covered cities from JSON input
    for _ in range(station_numbers):
        station = json.loads(input())

        # --- FIX 2: Handle inconsistent JSON keys safely ---
        name = station.get("name", station.get("Name"))
        cities = station.get("cities", station.get("Cities", []))

        stations[name] = set(cities)

    result = findStations(set(wanted_cities), stations)
    print(result)

if __name__ == "__main__":
    main()