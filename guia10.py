from typing import List

# 1. Archivos
# Ejercicio 1. Implementar en python:
ejemplo = "/home/Intro_programacion/Descargas/ejemplo.txt"
# 1. una funci ́on contarlineas(in nombre archivo : str) → int que cuenta la cantidad de l ́ıneas de texto del archivo dado
def contar_lineas(path: str) -> int:
    with open(path, "r") as file:
        return len(file.readlines())
# print(contar_lineas(ejemplo))

# 2. una funci ́on existePalabra(in palabra : str, in nombre archivo : str) → bool que dice si una palabra existe en un ar-
# chivo de texto o no
def pertenece(palabra: str, parrafo: str) -> bool:
    return True

def existe_palabra(palabra: str, path: str) -> bool:
    with open(path, "r") as file:
        for linea in file.readlines():
            if palabra in linea:
                return True
        else:
            return False
# print(existe_palabra("manzana", ejemplo))

# 3. una funci ́on cantidadApariciones(in nombre archivo : str, in palabra : str) → int que devuelve la cantidad de apari-
# ciones de una palabra en un archivo de texto
def separar_palabras(texto: str) -> List[str]:
    palabras: List[str] = []
    palabra: str = ""
    for letra in texto:
        if letra in [" ", "." "(", ")", ",", "\n", "?", "¿", "!", "¡", "#", "\""]:
            if len(palabra) > 0:
                palabras.append(palabra)
                palabra = ""
        else:
            palabra += letra
    return palabras

def cantidad_apariciones(path: str, palabra: str) -> int:
    # counter: int = 0
    # with open(path, "r") as file:
    #     for linea in file.readlines():
    #         for i in separar_palabras(linea):
    #             if palabra == i:
    #                 counter += 1
    # return counter
    longitud_palabra: int = len(palabra)
    counter: int = 0
    palabra_parcial: str = ""
    numero_de_linea: int = 0
    with open(path, "r") as file:
        for linea in file.readlines():
            numero_de_columna: int = (-longitud_palabra + 1)
            numero_de_linea += 1
            i: int = 0
            while len(linea) >= longitud_palabra and i < len(linea):
                if linea[i] == palabra[i]:
                    palabra_parcial += linea[i]
                    # print(palabra_parcial)
                    if palabra_parcial == palabra:
                        counter += 1
                        linea = linea[(i+1):]
                        numero_de_columna += i + 1
                        print(f"Línea: {numero_de_linea}. Columna: {numero_de_columna}")
                        i = 0
                        palabra_parcial = ""
                    else:
                        i += 1
                else:
                    linea = linea[1:]
                    palabra_parcial = ""
                    numero_de_columna += i + 1
                    i = 0
    return counter
print(cantidad_apariciones(ejemplo, "all too well"))

# Ejercicio 2. Dado un archivo de texto con comentarios, implementar una funci ́on clonarSinComentarios(innombre archivo : str)
# que toma un archivo de entrada y genera un nuevo archivo que tiene el contenido original sin las l ́ıneas comentadas. Para este
# ejercicio vamos a considerar comentarios como aquellas l ́ıneas que tienen un caracter # como primer caracter de la l ́ınea, o si no
# es el primer caracter, se cumple que todos los anteriores son espacios.
"""Ejemplo:
# esto es un comentario
# esto tambien
esto no es un comentario # esto tampoco"""
def clonar_sin_comentarios(path: str) -> str:
    with open(path, "r") as file:
        for linea in file.readlines():
            seguir: bool = True
            i: int = 0
            while seguir:
                if linea[i] == "#":
                    seguir = False
                elif linea[i] == " ":
                    i += 1
    return "hola"