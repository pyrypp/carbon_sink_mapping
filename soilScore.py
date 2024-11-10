import json

with open("plants.json", "r") as file:
    data = json.load(file)

def soilScore(soil: str, plant: str) -> float:
    cmp = data['Plants'][plant]['soils'][soil]
    return cmp
    

if __name__ == "__main__":
    cmp = soilScore("RG", "Oak")
    print(cmp)