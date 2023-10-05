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
    del cook_book["Фахитос"]
    #print(cook_list)
pprint(f"cook_book = {cook_book}")


def get_shop_list_by_dishes(dish_name, person_count):
    for dish in cook_book:
        for ingredients in cook_book[dish]:
            for ingredient, measure in ingredients.items():
                print(measure)
#     for dish in cook_book:
print(get_shop_list_by_dishes("Омлет",5))
#
#         else:
#             print("Такого блюда нет в меню")
#     print(my_cook_book)
#
# print(get_shop_list_by_dishes("Омлет", 7))
# print(new_cook)