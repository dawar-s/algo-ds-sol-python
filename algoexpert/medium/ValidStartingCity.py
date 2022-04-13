def validStartingCity(distances, fuel, mpg):
    city_count = len(distances)
    for i in range(city_count):
        fuel_remaining = 0
        j = i
        while True:
            travel_distance = distances[j]
            fuel_consumption = travel_distance / mpg
            fuel_in_vehicle = fuel[j] + fuel_remaining
            if fuel_consumption > fuel_in_vehicle:
                break
            fuel_remaining = round(fuel_in_vehicle - fuel_consumption, 1)
            j += 1
            j = j % city_count
            if j == i:
                return j


print(validStartingCity([5, 2, 3], [1, 0, 1], 5))