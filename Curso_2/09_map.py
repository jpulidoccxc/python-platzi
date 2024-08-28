numbers = [1, 2, 3, 4]
numbers_v2 = []

print(numbers)

for i in numbers:
  numbers_v2.append(i * 2)

print(numbers_v2)

# Map
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

# Map practice

items =[
  {'product': 'shirt',
  'price':120},
  {'product': 'pants',
  'price':160},
  {'product': 'jacket',
  'price':205}
]

prices = list(map(lambda item: item['price'], items))
print(prices)

# Map practice 2
def add_taxes(item):
  new_items = item.copy()
  new_items['taxes'] = new_items['price'] * .19
  return new_items

new_items = list(map(add_taxes, items))
print('New')
print(new_items)
print('Old')
print(items)