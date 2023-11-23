import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def dolar():

    url1 = 'https://www.google.com/search?q=euro&sca_esv=584893833&sxsrf=AM9HkKlrUbIyYGKqk_m54-vp10rSDgzI7g%3A1700757856227&ei=YIFfZcqJDfOp1sQP79W8yAc&oq=e&gs_lp=Egxnd3Mtd2l6LXNlcnAiAWUqAggAMgoQIxiABBiKBRgnMgoQIxiABBiKBRgnMgQQIxgnMgoQABiABBiKBRhDMhAQABiABBiKBRixAxiDARgKMgoQABiABBiKBRhDMgoQABiABBiKBRhDMgsQABiABBixAxiDATIKEAAYgAQYigUYQzIFEAAYgARIpwZQAFgAcAB4AZABAJgBcqABcqoBAzAuMbgBAcgBAPgBAeIDBBgAIEGIBgE&sclient=gws-wiz-serp'

    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'    
    }

    requisicao1 = requests.get(url=url1, headers=headers1)
    
    site1 = BeautifulSoup(requisicao1.text, 'html.parser')

    euro_cotacao = site1.find('span', class_="SwHCTb")
    euro_cotacao_formatado = euro_cotacao.text.replace(',', '.')

    url2 = 'https://www.google.com/search?q=dolar&oq=dolar&gs_lcrp=EgZjaHJvbWUyDggAEEUYJxg5GIAEGIoFMgwIARAjGCcYgAQYigUyDAgCEAAYQxiABBiKBTINCAMQABiDARixAxiABDIMCAQQABhDGIAEGIoFMhAIBRAAGIMBGLEDGIAEGIoFMgoIBhAAGLEDGIAEMg0IBxAAGIMBGLEDGIAEMgwICBAAGEMYgAQYigUyFggJEC4YgwEYxwEYsQMY0QMYgAQYigXSAQc1MzVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'

    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'    
    }

    requisicao2 = requests.get(url=url2, headers=headers2)
    
    site2 = BeautifulSoup(requisicao2.text, 'html.parser')

    dolar_cotacao = site2.find('span', class_="SwHCTb")
    dolar_cotacao_formatado = dolar_cotacao.text.replace(',', '.')
    resposta = {
        'valor_dolar': dolar_cotacao_formatado,
        'valor_euro': euro_cotacao_formatado,
    }
    return jsonify(resposta)

app.run()

