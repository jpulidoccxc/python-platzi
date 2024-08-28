#Error personalizado
age = 19

if age < 18:
  raise Exception('No se permiten menores de edad')

print('Edad validad')

# Error de python ZeroDivision
try:
  print(0 / 0)
except ZeroDivisionError as error:
  print('Error', error)
  
print('Hola')
# Error de python Assert
try:
  assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
  print('Error', error)
  
print('Hola2')
#Error personalizado 2 try except
age = 10
try:
  if age < 18:
    raise Exception('No se permiten menores de edad')
  
  print('Edad validad')
except Exception as error:
  print('Error', error)
  
print('Hola3')