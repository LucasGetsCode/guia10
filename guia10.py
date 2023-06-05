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
    longitud_palabra = len(palabra)
    # counter: int = 0
    # with open(path, "r") as file:
    #     for linea in file.readlines():
    #         for i in separar_palabras(linea):
    #             if palabra == i:
    #                 counter += 1
    # return counter
    counter: int = 0
    palabra_parcial = ""
    with open(path, "r") as file:
        for linea in file.readlines():
            i = 0
            while len(linea) >= longitud_palabra and i < len(linea):
                print(i)
                if linea[i] == palabra[i]:
                    palabra_parcial += linea[i]
                    print(linea)
                    if palabra_parcial == palabra:
                        counter += 1
                        linea = linea[(i+1):]
                        i = 0
                        palabra_parcial = ""
                        print(linea)
                    else:
                        i += 1
                else:
                    linea = linea[1:]
                    i = 0
    return counter
                
                



print(cantidad_apariciones(ejemplo, "all"))