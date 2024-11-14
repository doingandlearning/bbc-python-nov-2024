import json

# JavaScript Object Notation
#
# data = {
#     "name": "Harry",
#     "team": "App Admin",
#     "previous_python_experience": "Some",
#     "alive": True,
#     "no_of_toes": 10,
#     "projects": [
#         "app", "admin"
#     ]
# }
#
# with open("harry.json", "w") as f:
#     json.dump(data, f, indent=4)

harry = None

with open("harry.json") as f:
    harry = json.load(f)



print(f"harry has {harry["no_of_toes"]} toes.")