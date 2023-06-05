from typing import List

# 1. Archivos
# Ejercicio 1. Implementar en python:
ejemplo = "/home/Intro_programacion/Descargas/ejemplo.txt"
ejemplo2 = "/home/Intro_programacion/Descargas/ejemplo2.txt"
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
# print(cantidad_apariciones(ejemplo, "all too well"))

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
        texto_final: List[str] = []
        for linea in file.readlines():
            seguir: bool = True
            i: int = 0
            while seguir:
                if linea[i] == "#":
                    seguir = False
                elif linea[i] == " ":
                    i += 1
                else:
                    texto_final.append(linea)
                    seguir = False
    return "".join(texto_final)
# print(clonar_sin_comentarios(ejemplo2))

# Ejercicio 3. Dado un archivo de texto, implementar una funci ́on que escribe un archivo nuevo (‘reverso.txt‘) que tiene las
# mismas l ́ıneas que el original, pero en el orden inverso.
# Ejemplo: si el archivo original es
# Esta es la primer linea .
# Y esta es la segunda .
# debe generar:
# Y esta es la segunda .
# Esta es la primer linea .
def generar_reverso(path: str):
    texto_final: List[str] = []
    with open(path, "r") as file:
        for linea in file.readlines():
            texto_final.insert(0, linea)
    # new_path: str = "".join((path.split("/")[:-1]))
    texto_final[0] += "\n"
    if "\n" in texto_final[-1]:
        texto_final[-1] = "\n".join(texto_final[-1].split("\n")[:-1])
    with open("reverso.txt", "w") as file:
        for linea in texto_final:
            file.writelines(linea)
    # También podría usarse
    # for i in range(len(file.readlines()-1, -1, -1)): empieza desde la longitud-1, y llega hasta 0 (ya que es < y no <=)
# generar_reverso(ejemplo2)

# Ejercicio 4. Dado un archivo de texto y una frase (es decir, texto que puede estar separado por ’\n’), implementar una funci ́on
# que la agregue al final del archivo original (sin hacer una copia).
def agregar_frase(path: str, frase: str):
    frase_separada: List[str] = frase.split("\n")
    with open(path, "a") as file:
        for linea in frase_separada:
            file.write("\n"+linea)
# agregar_frase(ejemplo2, "Hola Don José\nHola Don Pepito\nChau a todos")

# Ejercicio 5. idem, pero agregando la frase al comienzo del archivo original (de nuevo, sin hacer una copia del archivo).
def agregar_frase_al_principio(path: str, frase: str):
    frase_separada: List[str] = frase.split("\n")
    texto: List[str] = []
    with open(path, "r") as file:
        texto = file.readlines()
        print(texto)
    with open(path, "w") as file:
        for linea in frase_separada:
            file.write(linea+"\n")
        print(texto)
        for linea in texto:
            file.write(linea)
    # También 
    # def agregar_frase_al_inicio(file_name, frase):
        # file = open(file_name, "r")
        # lines = [frase+"\n"] + file.readlines()
        # file.close()
        # file = open(file_name, "w")
        # for line in lines:
        #   file.write(line)
        # file.close()
# agregar_frase_al_principio(ejemplo2, "Hola Don José\nHola Don Pepito\nChau a todos")

# Ejercicio 6. Implementar una funci ́on que lea un archivo en modo *binario* y devuelva la lista de ’palabras legibles’. Vamos a
# definir una palabra legible como
# secuencias de texto formadas por numeros, letras mayusculas/minusculas y los caracteres ’ ’(espacio) y ’_’(guion bajo)
# que tienen longitud >= 5
# Una vez implementada la funci ́on, probarla con diferentes archivos binarios (.exe, .zip, .wav, .mp3, etc).
# Referencia: https://docs.python.org/es/3/library/functions.html#open
def palabras_legibles_binario(path: str):
    pass

# Cuando se abre un archivo el cursor está al principio. Si se lee una línea el cursor se mueve, si se sigue haciendo algo se hace desde ahí.
# O sea, si leo todas las líneas y quiero escribir algo, se escribe al final. Si leo una línea y después hago readlines() voy a leer todas menos la primera.
# Entonces para volver al principio se puede o cerrar y volver a abrir el archivo, o usar file.seek(0), haciendo que el cursor vaya a la línea 0

# Al trabajar con pilas, colas, etc. utilizar únicamente las funciones que te dan (por ej, no iterar)