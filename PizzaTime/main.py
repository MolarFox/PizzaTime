import json
import math
# Store input numbers
total_lexis = int(input('How many lexis: '))

# Display the sum
print(f"Wait while we do some quik maffs for {total_lexis} lexis")

minimum_lexis = 15
extra_lexis = total_lexis - minimum_lexis
bonus_garlic = math.ceil(extra_lexis/3)
bonus_wildcards = math.floor(extra_lexis/8)
bonus_pizza = math.ceil(extra_lexis*0.75) - bonus_wildcards
next_pizza_index = 0

staples = [
    "cheese", 
    "meat_lovers", 
    "vegan_spicy_veg_supreme", 
    "margherita", 
    "hawaiian", 
    "vegan_beef", 
    "regular_godfather", 
    "peri_peri", 
    "pepperoni", 
    "wild_cards"
]

base_order = {
    "pizzas": {
        "meat_lovers": 1,
        "hawaiian": 1,
        "cheese": 2,
        "margherita": 1,
        "vegan_spicy_veg_supreme": 1,
        "vegan_beef": 1,
        "regular_godfather": 1,
        "peri_peri": 1,
        "pepperoni": 1,
        "wild_cards": 2,
    },
    "sides": {
        "garlic_breads": 5
    }
}

base_order["pizzas"]["wild_cards"] += bonus_wildcards
base_order["sides"]["garlic_breads"] += bonus_garlic

while bonus_pizza > 0:
    base_order["pizzas"][staples[next_pizza_index]] += 1
    if next_pizza_index == 8:
        next_pizza_index = 0
    else:
        next_pizza_index += 1
    bonus_pizza -= 1

print(json.dumps(base_order, indent=4, sort_keys=True))