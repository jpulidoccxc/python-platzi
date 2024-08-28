import mod
  
data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  keys, values = mod.getPopulation()
  print(keys, values)
    
  country = input('Type Country => ')
  result = mod.populationByCountry(data, country)
  print(result)

if __name__ == '__main__':
  run()