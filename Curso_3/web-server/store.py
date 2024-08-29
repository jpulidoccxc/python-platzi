import requests

urlApi= 'https://fakestoreapi.com/products'

def get_categories():
    r = requests.get(f'{urlApi}/categories')
    print(f'Codigo respuesta HTTP: {r.status_code}')
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category)