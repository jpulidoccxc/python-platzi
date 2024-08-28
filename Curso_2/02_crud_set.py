set_countries = {'col', 'mex', 'bol'}

#size
size = len(set_countries)
print(size)

#in
print('col' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

#discard
set_countries.discard('arg')
print(set_countries)

#clear
set_countries.clear()
print(set_countries)