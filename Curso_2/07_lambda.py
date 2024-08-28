def increment(x):
  return x + 1


response = increment(2)
print(response)

#Lambda
increment_v2 = lambda x: x + 1
response = increment_v2(20)
print(response)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
text = full_name('Jefferson', 'Martinez')
print(text)
