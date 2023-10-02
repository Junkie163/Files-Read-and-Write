cook_book = {
    'Омлет': [{'ingedient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},
              {'ingedient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'},
              {'ingedient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}
              ],
    'Утка по-пекински': [{'ingedient_name': 'Утка', 'quantity': '1', 'measure': 'шт'},'\n',
                         {'ingedient_name': 'Вода', 'quantity': '2', 'measure': 'л'},
                         {'ingedient_name': 'Мед', 'quantity': '3', 'measure': 'ст. л'},
                         {'ingedient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}
                         ],
    'Запеченный картофель': [{'ingedient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'},
                             {'ingedient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч.'},
                             {'ingedient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'гр.'}
                             ]
}
with open('text.txt', 'w') as file:
    for dish, ingrs in cook_book.items():
        for ingr in ingrs:
            for ing in ingr.values():
                file.write(f'Название блюда: {dish} \nКоличество ингредиентов в блюде: \n{ing}')



