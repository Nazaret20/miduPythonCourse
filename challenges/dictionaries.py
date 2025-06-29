# # 🟢 Ejercicio 1: Contar palabras
# # Enunciado:
# # Dado un string, cuenta cuántas veces aparece cada palabra y devuelve un diccionario con esa información.

# # Ejemplo:
# # frase = "gato perro gato pez gato perro"
# # Resultado esperado: {'gato': 3, 'perro': 2, 'pez': 1}

# frase = "gato perro gato pez gato perro"

# def cuantas_palabras_hay(frase):
#     palabras = frase.split()
#     print(palabras)
#     resultado = {}

#     for palabra in palabras:
#         if palabra in resultado:
#             resultado[palabra] += 1
#         else:
#             resultado[palabra] = 1

#     return resultado


# print(cuantas_palabras_hay(frase))

# #---------------------------------

# # 🟢 Ejercicio 1: Contar letras
# # Crea una función llamada contar_letras que reciba una frase (string) y devuelva un diccionario con la cantidad de veces que aparece cada letra, ignorando los espacios y sin distinguir entre mayúsculas y minúsculas.

# # 🔍 Ejemplo:
# # contar_letras("Hola Mundo")
# # Debería devolver algo como:
# # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

# string = "Hooolaa Mmundo"

# def contar_letras(string):
#     conteo = {}
#     for letra in string:
#         letra = letra.lower()

#         if letra != ' ':
#             if letra in conteo:
#                 conteo[letra] += 1
#             else:
#                 conteo[letra] = 1
#     return conteo


# print(contar_letras(string))

# #---------------------------------

# # 🟡 Ejercicio 2: Calcular promedio de notas
# # Enunciado:
# # Tienes un diccionario con nombres de estudiantes y una lista de sus notas. Calcula el promedio de cada estudiante y devuelve un nuevo diccionario con su nombre y su promedio.

# # Ejemplo:
# # notas = {
# #     "Ana": [8, 7, 9],
# #     "Luis": [6, 5, 7],
# #     "Marta": [10, 9, 10]
# # }
# # # Resultado esperado: {'Ana': 8.0, 'Luis': 6.0, 'Marta': 9.67}

# notas = {
#     "Ana": [8, 7, 9],
#     "Luis": [6, 5, 7],
#     "Marta": [10, 9, 10],
#     "Marta F.": [1, 3, 5]
# }

# def notas_medias(notas):
#     nota_media = {}
#     suma = 0
#     media = 0

#     for alumno in notas:
#         suma = sum(notas[alumno])
#         media = suma / len(notas[alumno])
#         nota_media[alumno] = round(media, 2)

#     return nota_media

# print(notas_medias(notas))

# #---------------------------------

# # 🟠 Ejercicio 3: Fusionar dos diccionarios
# # Enunciado:
# # Tienes dos diccionarios con información de productos y precios. Si un producto está en ambos, suma sus valores. Devuelve un diccionario combinado.

# # Ejemplo:
# # productos_a = {"manzana": 3, "pera": 2}
# # productos_b = {"manzana": 2, "plátano": 4}
# # # Resultado esperado: {'manzana': 5, 'pera': 2, 'plátano': 4}

# productos_a = {"manzana": 3, "pera": 2}
# productos_b = {"manzana": 2, "plátano": 4}

# def inventario(productos_a, productos_b):
#     inventario_total = {}

#     for producto in productos_a:
#         if producto in inventario_total:
#             inventario_total[producto] += productos_a[producto]
#         else:
#             inventario_total[producto] = productos_a[producto]
#         print(producto)

#     for producto in productos_b:
#         if producto in inventario_total:
#             inventario_total[producto] += productos_b[producto]
#         else:
#             inventario_total[producto] = productos_b[producto]
#         print(producto)
#     print(inventario_total)


# inventario(productos_a, productos_b)

#---------------------------------

# 🔴 Ejercicio 4: Votación
# Enunciado:
# Tienes una lista con nombres de personas que votaron. Cuenta cuántos votos obtuvo cada persona.

# Ejemplo:

# votos = ["Ana", "Luis", "Ana", "Luis", "Marta", "Ana"]
# # Resultado esperado: {'Ana': 3, 'Luis': 2, 'Marta': 1}

votos = ["Ana", "Luis", "Ana", "Luis", "Marta", "Ana", "Ana"]

def recuento_votos(votos):
    recuento_final = {}

    for voto in votos:
        if voto in recuento_final:
            recuento_final[voto] += 1
        else:
            recuento_final[voto] = 1

    return recuento_final

print(recuento_votos(votos))