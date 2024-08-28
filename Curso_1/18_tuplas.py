numbers = (1,2,3,4,5)
strings = ('nico', 'zule', 'santi', 'jeff', 'nico')
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))

print('0 =>', numbers[0])

#Buscar dentro de la tupla
print(strings.index('zule'))
#Contar cuantas veces esta un elemento en la tupla
print(strings.count('nico'))
#Convertir tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))