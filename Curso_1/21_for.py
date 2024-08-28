#FOR
for element in range(1, 21):
  print(element)

print("=" * 80)

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

print("=" * 80)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

print("=" * 80)

product = {
  'name': 'Jefferson',
  'lastName': 'Pulido',
  'age': 21
}

for key in product:
  print(key, '=>', product[key])

print("=" * 80)

for key, value in product.items():
  print(key, '=>', value)

print("=" * 80)

people = [
  {
    'name': 'Jefferson',
    'lastName': 'Pulido',
    'age': 21
  },
  {
    'name': 'Juan',
    'lastName': 'Pulido',
    'age': 21
  },
  {
    'name': 'Jose',
    'lastName': 'Pulido',
    'age': 21
  }
]

for person in people:
  print(person)