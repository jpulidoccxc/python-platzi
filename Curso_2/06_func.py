#Funtions
def my_print(text):
  print(text)

my_print('Hola')

def suma(a, b):
  print(a + b)

suma(1, 5)
suma(10, 4)

#Funtion with return
def suma_return(a, b):
  sum = a + b
  return sum

response = suma_return(2, 2)
print(response)

#Funtion with return and multilpe returns
def find_volume(length=1, width=1, depth=1):
  return length * width * depth

result = find_volume(10, 20, 3)
print(result)

resultv2 = find_volume()
print(resultv2)

#scope
price = 100 #global scope
def increment():
  price = 200 #local scope
  price = price + 10
  print(price)
  return price

print(price)
resultIncrement = increment()