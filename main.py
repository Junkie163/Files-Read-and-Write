#def my_cook_book():
from pprint import  pprint
with open("text.txt", encoding="utf-8") as file:
    cook_book = {}
    for line in file.read().split(("\n\n")):
        #print(line)
        dish_name, *ingredients = line.split("\n")
        cook_list = []
        #print(ingredients)
        for ingredient in ingredients[1:]:
            ingredient_name, quantity, measure = ingredient.split(" | ")
            cook_list.append(
                {
                    "ingredient_name": ingredient_name,
                    "quantity": int(quantity),
                    "measure": measure,
                }
            )
        cook_book[dish_name] = cook_list


for dish_name, ingredients in cook_book.items():
   print(dish_name, ingredients, sep="\n")



def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient["quantity"] *= person_count
                new_cook.setdefault(ingredient["ingredient_name"], ingredient)
    meal_dict = {}
    for value in new_cook.values():
        name = value["ingredient_name"]
        del value["ingredient_name"]
        meal_dict[name] = value
    return  meal_dict


print(get_shop_list_by_dishes(["Омлет"], 5))

