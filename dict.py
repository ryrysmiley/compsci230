#dictionary practice
cereal={
"kind":"Cinnamon",
"Calories":270,
"Ingredients":["whole grain", "sugar", "rice flour"]
}
cereal["kind"]="Raisin"
"""
print(cereal)
print(cereal["kind"])
print(cereal["Ingredients"][0])
"""

print(dict.keys())
print(dict.values())
print(dict.get("Calories"))
print(dict.pop("kind"))
