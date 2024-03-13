house = {"Harry": "Gryffindor", "Draco": "Slytherin"}
house["Hermiione"] = "Gryffindor"
house["Andrie"] = "Slytherin"
for key, value in house.items():
    print(f"{key} is belong to  house {value}!")
# print(house)
# print(type(house))