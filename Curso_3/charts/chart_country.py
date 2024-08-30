import csv
import matplotlib.pyplot as plt
import re
import pandas as pd

def generate_bar_chart(labels, values, name):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.savefig('./imgs/pie_chart_docker_v.png')
    plt.close()

def populationCountryData():
  labels = []
  values = []
  country = input('Ingresa el pais: ')
  with open('./data.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = list(filter(lambda item: item['Country/Territory'] == country.capitalize(), reader))

    for key, value in data[0].items():
      if re.match('[0-9]{4} Population', key):
        labels.append(key.replace(' Population', ''))
        values.append(int(value))

    generate_bar_chart(labels, values, country)

def generate_south_america_pie_chart():
    labels = []
    values = []
    south_america_countries = [
      'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
      'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname',
      'Uruguay', 'Venezuela'
    ]

    with open('./data.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if row['Country/Territory'] in south_america_countries:
                labels.append(row['Country/Territory'])
                population = 0
                for key, value in row.items():
                    if re.match('[0-9]{4} Population', key):
                        population = int(value)
                values.append(population)

    generate_pie_chart(labels, values)

def populationWithPandas():
   df = pd.read_csv('./data.csv')
   df = df[df['Continent'] == 'Europe']

   countries = df['Country/Territory'].values
   percentages = df['World Population Percentage'].values
   generate_pie_chart(countries, percentages)

# populationCountryData()
# generate_south_america_pie_chart()
populationWithPandas()