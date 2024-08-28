import pkg.mod_1 as mod_1
import pkg.mod_2 as mod_2

print(mod_1.func_1())
print(mod_1.func_2())
print(mod_2.func_3())
print(mod_2.func_4())

n = []
for i in range(1, 6):
  if i <= 2:
    n.append(i - 1)

n = [i - 1 for i in range(1, 6) if i <= 2]

names = {'Nicolas', 'Miguel', 'Juan', 'Nicolas'} 
print(names) 

a = {1,2}
b = {2,3}
print(a - b)