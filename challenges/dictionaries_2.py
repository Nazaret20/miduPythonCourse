# 🔹 Ejercicio 2: Invertir diccionario
# Dado un diccionario donde las claves son nombres y los valores son edades, crea uno nuevo donde las claves sean las edades y los valores una lista de nombres que tengan esa edad.

# python
# Copiar
# Editar
# # Entrada:
# personas = {
#     "Ana": 25,
#     "Luis": 30,
#     "Marta": 25,
#     "Pedro": 30
# }

# Salida esperada:
# {25: ["Ana", "Marta"], 30: ["Luis", "Pedro"]}

personas = {
    "Ana": 25,
    "Luis": 30,
    "Marta": 25,
    "Pedro": 30,
    "Naza": 31
}

def edad_clave(personas):
    resultado = {}
    for persona, edad in personas.items():
        if edad in resultado:
            resultado[edad].append(persona)
        else:
            resultado[edad] = [persona]
    print(resultado)
    
edad_clave(personas)