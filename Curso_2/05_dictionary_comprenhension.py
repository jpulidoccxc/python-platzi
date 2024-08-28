import random

dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

#Dict comprenhension practice 1
dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
  population[country] = random.randint(1, 100)

print(population)

#Dict comprenhension practice 2
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

#Dict comprenhension practice 3
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

#Dict comprenhension conditionals

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 50}
print(result)

#Dict comprenhension conditionals practice 2
text = 'Hola, soy Jefferson'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique)
