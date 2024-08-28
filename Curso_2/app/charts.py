import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()
  
labels = ['Enero', 'Febrero', 'Marzo']
values = [1000, 2000, 8000]

if __name__ == '__main__':
  generate_bar_chart(labels, values)  
  #generate_pie_chart(labels, values)
