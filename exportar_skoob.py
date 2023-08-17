import requests
import csv

user_id = '1234568'
shelf_id = '0'
page = '1'
limit = '1000'

url = f'https://www.skoob.com.br/v1/bookcase/books/{user_id}/shelf_id:{shelf_id}/page:{page}/limit:{limit}'
resp = requests.get(url=url)
books = resp.json()['response']

for book in books:
    data_leitura = book['dt_leitura']
    paginas = book['paginas']
    nota = book['ranking']
    edicao = book['edicao']
    titulo = edicao['titulo']
    ano = edicao['ano'] 
    autor = edicao['autor']
    if (paginas == ""): paginas = edicao['paginas']

    dict_book = {'data_leitura': data_leitura, 'paginas': paginas, 'nota': nota, 'titulo': titulo, 'ano': ano, 'autor': autor}

    print(dict_book)