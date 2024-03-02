"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
from collections import defaultdict

nombre_archivo = "data.csv"


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_segunda_columna = 0

    with open(nombre_archivo, newline="") as archivo_csv:
        for linea in archivo_csv:
            partes = linea.strip().split("\t")
            segundo_elemento = partes[1]
            suma_segunda_columna += int(segundo_elemento)

    return suma_segunda_columna


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registros_por_letra = defaultdict(int)
    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            primera_letra = fila[0][0].upper()
            registros_por_letra[primera_letra] += 1

    registros_ordenados = sorted(registros_por_letra.items())

    return registros_ordenados


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_por_letra = defaultdict(int)

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                primera_letra = fila[0][0].upper()
                valor_segunda_columna = int(fila[1])
                suma_por_letra[primera_letra] += valor_segunda_columna

    suma_ordenada = sorted(suma_por_letra.items())

    return suma_ordenada


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros_por_mes = defaultdict(int)

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                fecha = fila[2]
                mes = fecha.split("-")[1]
                registros_por_mes[mes] += 1

    registros_ordenados = sorted(registros_por_mes.items(), key=lambda x: int(x[0]))

    return registros_ordenados


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    max_min_por_letra = defaultdict(lambda: (float("-inf"), float("inf")))

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                letra = fila[0]
                valor_columna_2 = int(fila[1])
                max_min_por_letra[letra] = (
                    max(max_min_por_letra[letra][0], valor_columna_2),
                    min(max_min_por_letra[letra][1], valor_columna_2),
                )

    max_min_lista = [
        (letra, max_valor, min_valor)
        for letra, (max_valor, min_valor) in max_min_por_letra.items()
    ]
    max_min_lista_ordenada = sorted(max_min_lista, key=lambda x: x[0])


    return max_min_lista_ordenada


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    min_max_por_clave = defaultdict(lambda: (float("inf"), float("-inf")))

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                diccionario_codificado = fila[4]
                elementos = diccionario_codificado.split(",")
                for elemento in elementos:
                    clave, valor_str = elemento.split(":")
                    valor = int(valor_str)
                    min_max_por_clave[clave] = (
                        min(min_max_por_clave[clave][0], valor),
                        max(min_max_por_clave[clave][1], valor),
                    )

    min_max_lista = [
        (clave, min_valor, max_valor)
        for clave, (min_valor, max_valor) in min_max_por_clave.items()
    ]

    min_max_lista_ordenada = sorted(min_max_lista)

    return min_max_lista_ordenada


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letras_por_valor_columna2 = defaultdict(list)

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                valor_columna2 = int(fila[1])
                letra_columna1 = fila[0]
                letras_por_valor_columna2[valor_columna2].append(letra_columna1)

    lista_tuplas = [
        (valor, letras) for valor, letras in letras_por_valor_columna2.items()
    ]

    lista_tuplas_ordenada = sorted(lista_tuplas)
    
    return lista_tuplas_ordenada


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    letras_por_valor_columna2 = defaultdict(set)

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                valor_columna2 = int(fila[1])
                letra_columna1 = fila[0]
                letras_por_valor_columna2[valor_columna2].add(letra_columna1)

    lista_tuplas = [
        (valor, sorted(letras)) for valor, letras in letras_por_valor_columna2.items()
    ]
    lista_tuplas_ordenada = sorted(lista_tuplas)
    
    return lista_tuplas_ordenada


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    frecuencia_claves_columna5 = defaultdict(int)

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if fila:
                diccionario_codificado = fila[4]
                elementos = diccionario_codificado.split(",")
                for elemento in elementos:
                    clave, _ = elemento.split(":")
                    frecuencia_claves_columna5[clave] += 1

    registros_ordenados = dict(sorted(frecuencia_claves_columna5.items()))

    return registros_ordenados


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultado = []

    with open("data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')

        for row in reader:
            letra = row[0]
            elementos_columna_4 = len(row[3].split(","))  
            elementos_columna_5 = len(row[4].split(","))  
            resultado.append((letra, elementos_columna_4, elementos_columna_5))
    
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    with open("data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')

        for row in reader:
            letras = row[3].split(",")  
            for letra in letras:
                letra = letra.strip()  
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + int(row[1])  

    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))
    
    return suma_por_letra_ordenada


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_columna_1 = {}

    with open("data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')

        for row in reader:
            columna_1 = row[0]
            valores_columna_5 = row[4].split(",") 
            for par in valores_columna_5:
                clave, valor = par.split(":") 
                suma_por_columna_1[columna_1] = suma_por_columna_1.get(columna_1, 0) + int(valor)  
    
    suma_por_columna_ordenada = dict(sorted(suma_por_columna_1.items()))
    
    return suma_por_columna_ordenada


# def main():
    # print(pregunta_01())
    # print(pregunta_02())
    # print(pregunta_03())
    # print(pregunta_04())
    # print(pregunta_05())
    # print(pregunta_06())
    # print(pregunta_07())
    # print(pregunta_08())
    # print(pregunta_09())
    # print(pregunta_10())
    # print(pregunta_11())
    # print(pregunta_12())

def main():
    pregunta_01()
    pregunta_02()
    pregunta_03()
    pregunta_04()
    pregunta_05()
    pregunta_06()
    pregunta_07()
    pregunta_08()
    pregunta_09()
    pregunta_10()
    pregunta_11()
    pregunta_12()


if __name__ == "__main__":
    main()
