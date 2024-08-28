#READ
'''
with open('./text.txt', 'r') as f:
  #print(f.read())
  print(f.readline())
  print(f.readline())
  print(f.readline())

with open('./text.txt', 'r') as f:
  for line in f:
    print(line)
'''
#WRITE
'''
with open('./text.txt', 'r+') as f:
  for line in f:
    print(line)
  f.write('Nuevas cosas en este archivo\n')
'''
#READ CSV
