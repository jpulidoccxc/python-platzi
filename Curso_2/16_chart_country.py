import csv
import matplotlib.pyplot as plt
import re

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def practice():
  labels = []
  values = []
  country = input('Ingresa el pais: ')
  with open('./app/data.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = list(filter(lambda item: item['Country/Territory'] == country.capitalize(), reader))

    for key, value in data[0].items():
      if re.match('[0-9]{4} Population', key):
        labels.append(key.replace(' Population', ''))
        values.append(int(value))

    generate_bar_chart(labels, values)

practice()
