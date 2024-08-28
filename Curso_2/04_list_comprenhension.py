numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

# List Comprehension

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)