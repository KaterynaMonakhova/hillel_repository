from operator import itemgetter

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
data_sorted = sorted(data, key=itemgetter('age'))
new_dict = {}
for i in data_sorted:
    for key, value in i.items():
        if 'city' in key:
            new_dict[value] = []
for elem in data_sorted:
    if elem['city'] in new_dict:
        new_dict[elem.pop('city')].insert(-1, elem)
print(new_dict)
