import pandas as pd
import re
import signal
import sys


class GeneroNoEncontrado(Exception):
    print('\nNO ENCONTRADO')


def handler_signal(signal,frame):

    print("\n\n [!] out .......\ n")

    sys.exit(1)

signal.signal(signal.SIGINT,handler_signal)


def extract():
    df = pd.read_csv('songs_normalize.csv', sep=',')
    return df


def transform(df):

    categorias = ['artist', 'year', 'genre', 'popularity']
    cat = True
    while cat:

        print('Se recomiendan canciones en base a las siguientes categorías')

        for i in range(len(categorias)):
            print(f'{categorias[i]}')

        entrada = input('¿Cuál desea? ')

        for i in categorias:
            if re.match(entrada, i, re.I) != None:
                parametro = i
                cat = False

    posibilidades = df[parametro].unique()

    print('Posibilidades: ')
    for i in posibilidades: print(i)
    entrada = input('¿Cuál desea?: ')

    genero = []

    for i in posibilidades:
        regex = re.match(entrada, str(i), re.I)

        if regex:
            genero.append(i)

    if genero != []:

        canciones = []
        tamano = df.shape
        x = tamano[0]

        for i in range(x-1):

            if df.loc[i, parametro] in genero:
                canciones.append(df.song.loc[i])

    else:
        raise GeneroNoEncontrado(f'No se encontró {entrada}')
    return canciones


def load(data):

    print()
    for song in data:
        print(song)


if __name__ == '__main__':
    df = extract()
    try:
        data = transform(df)
        load(data)
    except GeneroNoEncontrado as error:
        print(error)
