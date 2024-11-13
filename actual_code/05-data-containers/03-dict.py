# dictionary, key/value, growable, ordered, mutable

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

capitals = {
    "England": {"capital_city": "London", "population": 60_000_000},
    "Scotland": "Edinburgh",
    "Wales": "Cardiff",
    "Northern Ireland": "Belfast"
}

print(capitals["England"])

for country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")

print(capitals.values())
print(capitals.keys())
print(capitals.items())

print("England" in capitals)  # is it a key - not is it in the dictionary somewhere!
print("Edinburgh" in capitals)