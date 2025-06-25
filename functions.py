# # 📌 FUNCIONES SOBRE NÚMEROS Y RANGOS
# # 1. Suma de números en un rango
# # Crea una función que reciba dos números (inicio y fin) y devuelva la suma de todos los números desde inicio hasta fin (inclusive).
# print("Ejercicio 1")

# def suma(*args):
#     suma = 0
#     for num in args:
#         suma += num
#     return suma

# print(suma(*range(1, 11)))

# # 2. Tabla de multiplicar
# # Crea una función que reciba un número y muestre su tabla de multiplicar del 1 al 10.
# print("Ejercicio 2")
# user_num = int(input("Introduce un número: "))

# def tabla_multiplicar(user_num):
#     for numero in range(1, 11):
#         resultado = user_num * numero
#         print(f"{user_num} x {numero} = {resultado}")

# tabla_multiplicar(user_num)

# # 3. Factorial de un número
# # Crea una función que reciba un número entero positivo y devuelva su factorial.
# # Ejemplo: factorial(5) → 120 (porque 5×4×3×2×1 = 120).
# print("Ejercicio 3")
# num_user = int(input("Introduce un número: "))

# def factorial(num_user):
#     contador = 1
#     factorial = 1

#     while contador <= num_user:
#         factorial *= contador
#         contador += 1
#         print(factorial)

# factorial(num_user)

# # 4. Números primos hasta N
# # Crea una función que reciba un número entero n y devuelva una lista con todos los números primos menores o iguales que n.
# print("Ejercicio 4")
# user_num = int(input("Dime un número: "))

# def numeros_primos(user_num):
#     for primo in range(2, user_num + 1):
#         es_primo = True
#         for i in range(2, primo):
#             if primo % i == 0:
#                 es_primo = False
#                 break
#         if es_primo:
#             print(primo)


# numeros_primos(user_num)

# # 📌 FUNCIONES CON LISTAS
# # 5. Calcular la media de una lista
# # Crea una función que reciba una lista de números y devuelva su media (promedio).
# # Ejemplo: [10, 20, 30] → 20.
# print("Ejercicio 5")

# numbers = [10, 20, 30, 40, 50]

# def media_de_lista(numbers):
#     suma = 0
#     for number in numbers:
#         suma += number
#     media = suma / len(numbers)
#     print(media)

# media_de_lista(numbers)

# # 6. Buscar el número máximo en una lista
# # Crea una función que reciba una lista de números y devuelva el número más grande.
# print("Ejercicio 6")

# nums = [15, 5, 25, 10, 20]

# def numero_alto(nums):
#     maximo = float('-inf')
#     for num in nums:
#         if num > maximo:
#             maximo = num
#     print(maximo)

# numero_alto(nums)

# # 7. Filtrar palabras largas
# # Crea una función que reciba una lista de palabras y devuelva una nueva lista con solo aquellas que tengan más de 5 letras.

# print("Ejercicio 7")

# palabras_de_5 = ["gato", "elefante", "casa", "murciélago", "sol", "jirafa", "mariposa", "perro", "avión"]

# def palabras_largas(palabras_de_5):
#     cinco_letras = []
#     for palabra in palabras_de_5:
#         if len(palabra) > 5:
#             cinco_letras.append(palabra)
#     return cinco_letras

# palabras_largas(palabras_de_5)

# # 8. Contar palabras que empiezan con una letra
# # Crea una función que reciba una lista de palabras y una letra, y devuelva cuántas palabras empiezan por esa letra (sin diferenciar mayúsculas/minúsculas).

# print("Ejercicio 8")

# letra_user = input("Introduce una letra: ")
# unas_palabras = ["Casa", "árbol", "sol", "Elefante", "luna", "coche", "Armario"]

# def simplificar(letra):
#     acentos = {
#         'á': 'a',
#         'é': 'e',
#         'í': 'i',
#         'ó': 'o',
#         'ú': 'u',
#         'Á': 'a',
#         'É': 'e',
#         'Í': 'i',
#         'Ó': 'o',
#         'Ú': 'u'
#     }
#     return acentos.get(letra, letra).lower()

# def palabras_por_letra(letra_user, unas_palabras):
#     palabras = []
#     contador = 0
#     letra_sin_acento = simplificar(letra_user)

#     for una_palabra in unas_palabras:
#         if simplificar(una_palabra[0]) == letra_sin_acento:
#             palabras.append(una_palabra)
#             contador += 1
#     print(palabras)
#     print(contador)

#     palabra_singular = "palabra" if contador == 1 else "palabras"
#     verbo_singualr = "es" if len(palabras) == 1 else "son"
#     result = " ".join(palabras)

#     return f"Hay {contador} {palabra_singular}, y {verbo_singualr}: {result}"

# print(palabras_por_letra(letra_user, unas_palabras))

# # 📌 FUNCIONES LÓGICAS
# # 9. Calculadora simple
# # Crea una función que reciba dos números y un operador (+, -, *, /) y devuelva el resultado de la operación.
# # Debe manejar el caso de división entre cero.

# # 10. Año bisiesto
# # Crea una función que reciba un año y devuelva True si es bisiesto, o False si no lo es.
# # (Es bisiesto si es divisible por 4, excepto si también es divisible por 100 y no por 400).

# # 11. Clasificar edades
# # Crea una función que reciba una edad y devuelva una categoría:

# # 0-2: "Bebé"

# # 3-12: "Niño/a"

# # 13-17: "Adolescente"

# # 18-64: "Adulto/a"

# # 65+: "Adulto/a mayor"