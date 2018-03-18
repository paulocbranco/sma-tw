# Autor: Paulo Branco (2018)
# Script necessário para recolher dados para o trabalho da disciplina Social Media Analytics (MGIBI@NOVAIMS)

# Para executar: python3 sma-tw.py

# instalar as seguintes livrarias
# pip install python-twitter
# pib install pandas

# Para mais informação sobre esta livraria consultar
# https://python-twitter.readthedocs.io/en/latest/index.html

import twitter
import datetime as dt
from pandas.core.frame import DataFrame
from urllib.parse import unquote
import os

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxx'


def main():
    search('WorldCup+2018')


def get_api():
    api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return api


def search(query=None, raw_query=None, api=None, total=None):
    next_results = None
    try:
        if api is None:
            api = get_api()

        if query is not None:
            print('Procurar tweets: ' + query)
            tweets = api.GetSearch(term=query, count=100, return_json=True)
        else:
            tweets = api.GetSearch(raw_query=raw_query, return_json=True)

        if total is None:
            count = tweets['search_metadata']['count']
        else:
            count = total + tweets['search_metadata']['count']

        if 'next_results' in tweets['search_metadata']:
            data = str(tweets['search_metadata']['next_results'])
            next_results = data.split('?')[1]

        print('Tweets encontrados:', count, end='\r')
        name = tweets['search_metadata']['query']
        filename = makedir(name) + get_filename(name)
        write_tweets(tweets['statuses'], filename)
        if next_results is not None:
            search(raw_query=next_results, api=api, total=count)
        else:
            print('Total de tweets encontrados:', count)

    except Exception as ex:
        print('Erro encontrado:' + ex)


def get_filename(name):
    d = dt.datetime.now()
    day = '{0}-{1:0>2}-{2:0>2}'.format(d.year, d.month, d.day)
    filename = unquote(name).replace('+', '_')
    return '{}_{}.csv'.format(filename, day)


def write_tweets(tweets, filename):
    df = DataFrame(tweets)
    with open(filename, 'a') as f:
        df.to_csv(f, sep='\t', index=False, encoding='utf-8')


def makedir(name):
    dirname = unquote(name).replace('+', '_') + '/'
    os.makedirs(os.path.dirname(dirname), exist_ok=True)
    return dirname


if __name__ == '__main__':
    main()
