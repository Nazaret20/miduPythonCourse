import os
os.system("cls")

##
#EJERCICIOS (for)
##

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16,17,18,19,20]
for num in numbers:
    if num % 2 == 0:
        print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
suma = 0
media = 0

for numero in numeros:
    suma += numero
media = suma / len(numeros)

print(media)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

nums = [15, 5, 25, 10, 20]
mayor = float('-inf')

for numm in nums:
    if numm > mayor:
        mayor = numm
print(mayor)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]

palabras_mayores = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_mayores)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

words = ["casa", "arbol", "sol", "elefante", "luna", "coche", "Armario"]

letter = input("Introduce una letra: ")
times = 0
lista = []
result = ""

for word in words:
    if word[0].lower() == letter.lower():
        times += 1
        lista.append(word)
result = " ".join(lista)

una_o_dos = "palabra" if times == 1 else "palabras"
verbo = "es" if times == 1 else "son"

print(f"Hay {times} {una_o_dos} con la letra {letter} y {verbo}: {result}")
