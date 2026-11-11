cities = []

while True:
    city = input("Enter a city (or type done): ").strip()
    if city.lower() == "done":
        break
    if city:
        cities.append(city)

print("Cities:", cities)

remove_city = input("City to remove (or press Enter to skip): ").strip()
if remove_city in cities:
    cities.remove(remove_city)

print("Final cities:", cities)