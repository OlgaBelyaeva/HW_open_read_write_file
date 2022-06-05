# Открытие и чтение файла, запись в файл
# Задача 1 и 2

from pprint import pprint
import os

base_path = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(base_path, file_name)

with open(full_path) as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        number_of_ingred = int(file.readline())
        inrged_in_dish = []
        for i in range(number_of_ingred):
            ingreg_dict = {}
            ingred = file.readline().strip().split('|')
            ingreg_dict['ingredient_name'] = ingred[0]
            ingreg_dict['quantity'] = ingred[1]
            ingreg_dict['measure'] = ingred[2]
            inrged_in_dish.append(ingreg_dict)
        cook_book[dish] = inrged_in_dish
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        # if dish in cook_book.keys():
        for ingredient in cook_book[dish]:
            ingred_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = int(ingredient['quantity']) * person_count
            if ingred_name not in shop_list_by_dishes.keys():
                shop_list_by_dishes[ingred_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list_by_dishes[ingred_name]['quantity'] += quantity
    return shop_list_by_dishes

pprint(cook_book)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 2))