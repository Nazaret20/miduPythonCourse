import os
os.system("cls")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

num = 10
while num > 0:
    print(num)
    num -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

contador = 0
pares_sum = 0

while contador < 20:
    contador += 1
    if contador % 2 == 0:
        pares_sum += contador

print(contador)
print(pares_sum)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

while True:
    try:
        number = int(input("Dime un número entero y positivo\n"))
        if number <= 0:
            print("Debe ser mayor a 0")
            continue
        break
    except ValueError:
        print("Debes introducir un número")

contador = 1
factorial = 1

while contador <= number:
    factorial *= contador
    contador += 1

print(factorial)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
    password = input("Introduce tu contraseña\n")
    if len(password) >= 8:
        print("Contraseña válida")
        break
    print("Debe tener al menos 8 carácteres")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

random_num = int(input("Introduce un número\n"))

multiply = 1
result= 0

while multiply <= 10:
    result = random_num * multiply
    print(f"{random_num} x {multiply} = {result}")
    multiply += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

N = int(input("Introduce un número entero positivo:\n"))

num = 2

while num <= N:
    es_primo = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(num)
    num += 1
