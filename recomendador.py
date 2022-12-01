import pandas as pd
import re
import signal
import sys


class GeneroNoEncontrado(Exception):

    # Definimos una clase excepción en caso de que el usuario
    # introduzca un filtro que no se encuentre en el dataset

    pass


def handler_signal(signal,frame):

    # Realizamos una salida controlada del programa en caso de que
    # el usuario presione control C

    print("\n\n [!] out .......\ n")

    sys.exit(1)

signal.signal(signal.SIGINT,handler_signal)


def extract():

    # Se extraen los datos del dataset con las canciones

    df = pd.read_csv('songs_normalize.csv', sep=',')
    return df


def transform(df):

    # Se transforman para quedarse solo con aquellas canciones que cumplan
    # los filtros del usuario

    # Se dejará al usuario filtrar pos las categorías de artista, año
    # género y popularidad

    categorias = ['artist', 'year', 'genre', 'popularity']
    cat = True

    # Se pregunta al usuario por el nombre de la categoría de recomendación
    # que desea hasta que introduzca una válida

    while cat:

        print('Se recomiendan canciones en base a las siguientes categorías')

        for i in range(len(categorias)):
            print(f'{categorias[i]}')

        entrada = input('¿Cuál desea? ')

        # Se comprueba si el nombre de la categoría introducida por el usuario es
        # válida.

        for i in categorias:
            if re.match(entrada, i, re.I) != None:
                parametro = i
                cat = False

    # Se extraen las distintas posibilidades dentro de la categoría seleccionada

    posibilidades = df[parametro].unique()

    print('Posibilidades: ')
    for i in posibilidades:
        print(i)
    entrada = input('¿Cuál desea?: ')

    genero = []

    # Se analiza el segundo filtro introducido por el usuario
    for i in posibilidades:
        regex = re.match(entrada, str(i), re.I)

        if regex:
            genero.append(i)

    # En caso de que el segundo filtro sea válido se extraen
    # todas las canciones que cumplan el filtro y se añaden a la lista
    # de canciones

    if genero != []:

        canciones = []
        tamano = df.shape
        x = tamano[0]

        for i in range(x-1):

            if df.loc[i, parametro] in genero:
                canciones.append(df.song.loc[i])

    # Si no se encuentra el filtro solicirado se muestra un mensaje de error
    # por pantalla y se lanza una excepción

    else:
        raise GeneroNoEncontrado(f'No se encontró {entrada}')

    # Se devuelven las canciones recomendadas
    return canciones


def load(data):

    # Se muestran las canciones recomendadas

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
