print("Calculate fuel consumption:")
feed = input("Enter travel distance(kilometers): ")
Distance = int(feed)
feed = input("Enter fuel usage(liters): ")
FuelUsage = int(feed)
Consumption = FuelUsage / Distance * 100
print("Fuel consumption is", int(Consumption), "l per 100km")