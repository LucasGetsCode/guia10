from typing import List
import os


# 1. Archivos
# Ejercicio 1. Implementar en python:
# ejemplo = "/home/Intro_programacion/Descargas/ejemplo.txt"
# ejemplo2 = "/home/Intro_programacion/Descargas/ejemplo2.txt"
ejemplo = "ejemplo.txt"
ejemplo2 = "ejemplo2.txt"
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
def palabras_legibles_binario(path: str) -> List[str]:
    def es_palabra_valida(palabra):
        if len(palabra) >= 5:
            for letra in palabra:
                if letra not in "0123456789abcdefghijklmnñopqrstuvwxzABCDEFGHIJKLMNÑOPQRSTUVWXZ_":
                    return False
            return True
        else:
            return False

    palabras: List[str] = []
    with open(path, "r") as file:
        for linea in file.readlines():
            for palabra in separar_palabras(linea):
                if es_palabra_valida(palabra):
                    palabras.append(palabra)

    return palabras
# print(palabras_legibles_binario("../__pycache__/Guia8Listas.cpython-37.pyc"))

########
# Cuando se abre un archivo el cursor está al principio. Si se lee una línea el cursor se mueve, si se sigue haciendo algo se hace desde ahí.
# O sea, si leo todas las líneas y quiero escribir algo, se escribe al final. Si leo una línea y después hago readlines() voy a leer todas menos la primera.
# Entonces para volver al principio se puede o cerrar y volver a abrir el archivo, o usar file.seek(0), haciendo que el cursor vaya a la línea 0

# Al trabajar con pilas, colas, etc. utilizar únicamente las funciones que te dan (por ej, no iterar)
########

# 2. Pilas 
# Ejercicio 8. Implementar una funci´on generarNrosAlAzar(in n : int, in desde : int, in hasta : int) → list[int] que genere
# una lista de n numeros enteros al azar en el rango [desde, hasta]. Pueden user la funci´on random.sample()
from random import sample
def generar_numeros_al_azar(n: int, desde: int, hasta: int) -> List[int]:
    rango = range(desde, hasta+1)
    return sample(rango, n)
# print(generar_numeros_al_azar(5, 10, 20))

# Ejercicio 9. Usando la funci´on del punto anterior, implementar otra funci´on que arme una pila con los numeros generados al
# azar. Pueden usar la clase LifoQueue() que es un ejemplo de una implementaci´on b´asica:
# from queue import LifoQueue as Pila
# p = Pila()
# p.put(1)             # apilar
# elemento = p.get ()   # desapilar
# p.empty()            # vacia ?
from queue import LifoQueue as Pila
def pila_azarosa(n: int, desde: int, hasta: int) -> Pila:
    n = max(1, n)
    pila = Pila()
    for i in generar_numeros_al_azar(n, desde, hasta):
        pila.put(i)
    return pila
# print(pila_azarosa(5, 10, 20))

# Ejercicio 10. Implementar una funci´on cantidadElementos(in p : pila) → int que, dada una pila, cuente la cantidad de
# elementos que contiene.
def cantidad_de_elementos(p: Pila) -> int:
    i: int = 0
    while not p.empty():
        i += 1
        p.get()
    return i
# print(cantidad_de_elementos(pila_azarosa(10, 10, 20)))

# Ejercicio 11. Dada una pila de enteros, implementar una funci´on buscarElMaximo(in p : pila) → int que devuelva el m´aximo elemento.
def buscar_el_maximo(p: Pila) -> int:
    maximo: int = p.get()
    while not p.empty():
        maximo = max(maximo, p.get())
    return maximo
# print(buscar_el_maximo(pila_azarosa(5, 10, 20)))

# Ejercicio 12. Implementar una funci´on estaBienBalanceada(in s : str) → bool que dado un string con una formula aritm´etica
# sobre los enteros, diga si los par´entesis estan bien balanceados. Las f´ormulas pueden formarse con:
# los numeros enteros
# las operaciones basicas +, −, x y /
# parentesis
# espacios
# Entonces las siguientes son formulas aritm´eticas con sus par´entesis bien balanceados:
# 1 + ( 2 x 3 = ( 2 0 / 5 ) )
# 10 * ( 1 + ( 2 * (-1)))
# Y la siguiente es una formula que no tiene los par´entesis bien balanceados:
# 1 + ) 2 x 3 ( ( )
def esta_bien_balanceada(s: str) -> bool:
    def sacar_espacios(texto: str) -> str:
        res = ""
        for i in texto:
            if i != " ":
                res += i
        return res

    parentesis_abiertos: int = 0
    ultimo_caracter: str = ""
    s = sacar_espacios(s)
    for i in s:
        if i == ")":
            if parentesis_abiertos > 0:
                parentesis_abiertos -= 1
            else:
                return False
            if ultimo_caracter in "+-*/":
                return False
        if i == "(":
            parentesis_abiertos += 1
        if ultimo_caracter == "(" and i in "*/)":
            return False
        ultimo_caracter = i
    return True
# print(esta_bien_balanceada("(1)+(3*2)/(5)*6"))

# 3. Colas
# Ejercicio 13. Usando la funci´on generarNrosAlAzar() definida en la secci´on anterior, implementar una funci´on que arme una
# cola de enteros con los numeros generados al azar. Pueden usar la clase Queue() que es un ejemplo de una implementaci´on b´asica:
# from queue import Queue as Cola
# c = Cola()
# c.put(1)           # encolar
# elemento = c.get() # desencolar()
# c.empty()          # vacia ?
from queue import Queue as Cola
def cola_azarosa(n: int, desde: int, hasta: int) -> Cola:
    n = max(1, n)
    pila = Cola()
    for i in generar_numeros_al_azar(n, desde, hasta):
        pila.put(i)
    return pila
# print(cola_azarosa(5,10,20))

# Ejercicio 14. Implementar una funci´on cantidadElementos(in c : cola) → int que, dada una cola, cuente la cantidad de
# elementos que contiene. Comparar con la versi´on usando pila.def cantidad_de_elementos(p: Pila) -> int:
def cantidad_de_elementos_cola(p: Cola) -> int:
    i: int = 0
    while not p.empty():
        i += 1
        p.get()
    return i
# print(cantidad_de_elementos_cola(cola_azarosa(5,10,20)))

# Ejercicio 15. Dada una cola de enteros, implementar una funci´on buscarElMaximo(in c : cola) → int que devuelva el m´aximo
# elemento. Comparar con la versi´n usando pila.
def buscar_el_maximo_cola(q: Cola) -> int:
    p = q
    maximo: int = p.get()
    while not p.empty():
        maximo = max(maximo, p.get())           ####### NO RESPETA EL "IN" DE LA ESPECIFICACIÓN
    print(cantidad_de_elementos_cola(q))
    return maximo
# print(buscar_el_maximo_cola(cola_azarosa(5,10,20)))

# Ejercicio 16. Bingo: un cart´on de bingo contiene 12 n´umeros al azar en el rango [0, 99].
# 1. implementar una funci´on armarSecuenciaDeBingo() → Cola[int] que genere una cola con los n´umeros del 0 al 99 ordenados
# al azar.
def armar_secuencia_de_bingo() -> "Cola[int]":
    numeros = list(range(0,100))
    cola = Cola()
    while len(numeros) > 0:
        i = sample(range(len(numeros)), 1)[0]
        cola.put(numeros.pop(i))
    return cola
# print(cantidad_de_elementos_cola(armar_secuencia_de_bingo()))

# 2. implementar una funci´on jugarCartonDeBingo(in carton : list[int], in bolillero : cola[int]) → int que toma un cart´on
# de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de jugadas de
# ese bolillero que se necesitan para ganar.
def jugar_carton_de_bingo(carton: List[int], bolillero: "Cola[int]") -> int:
    jugadas: int = 0
    while not bolillero.empty():
        bola = bolillero.get()
        if bola in carton:
            carton.remove(bola)
        jugadas += 1
        if len(carton) == 0:
            return jugadas
    return -1
# print(jugar_carton_de_bingo([1,2,3,4,5,6,7,8,9,10,11,12], armar_secuencia_de_bingo()))

# Ejercicio 17. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
# para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente
# y requiere atenci´on inmediata) junto con su nombre y la especialidad medica que le corresponde.
# Implementar la funci´on nPacientesUrgentes(in c : Cola[(int, str, str)]) → int que devuelve la cantidad de pacientes de
# la cola que tienen prioridad en el rango [1, 3].
def pacientes_urgentes(c: "Cola[tuple]") -> int:
    pass