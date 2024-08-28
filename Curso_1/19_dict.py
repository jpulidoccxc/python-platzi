my_dict = {}
print(type(my_dict))

my_dict = {
  'carro': 'Lambo',
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('ages'))
print('carro' in my_dict)
print('avion' in my_dict)

print("=" * 80)
#MODIFICAR DICT
person = {
  'name': 'Jefferson',
  'last_name': 'Pulido',
  'langs': ['python', 'javascript'],
  'age': 21,
  'country': 'Colombia'
}
print(person)
#Modificar un valor
person['name'] = 'Stiven'
#Agregar un valor
person['langs'].append('rust')
print(person)
#Elimiinar un par clave valor
del person['last_name']
person.pop('age')
print(person)

#Obtener items
print(person.items())
#Obtener keys
print(person.keys())
#Obtener values
print(person.values())