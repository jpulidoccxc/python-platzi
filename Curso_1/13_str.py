text = 'Ella sabe Python'
print('Java esta en texto?: ', 'Java' in text)
print('Python esta en texto?: ', 'Python' in text)

print('Longitud de texto: ', len(text))
print('Texto en mayusculas: ', text.upper())
print('Texto en minusculas: ', text.lower())
print('Contar cuantas veces esta una letra en el texto: ', text.count('a'))
print('Cambiar mayusculas por minusculas y viceversa: ', text.swapcase())
print('Texto inicia con la palabra "Ella": ', text.startswith('Ella'))
print('Texto finaliza con la palabra "Rust": ', text.endswith('Rust'))
print('Reemplazar la palabra "Python" por "Go": ', text.replace('Python','Go'))

text_2 = 'este es un titulo'
print('Texto en inicial mayuscula: ', text_2.capitalize())
print('Texto en iniciales mayusculas: ', text_2.title())
print('Texto es un digito: ', text_2.isdigit())