# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

number_one, number_two = input("Introduce dos número al azar del 1 al 10\n").split()
print(f"Has elegido {number_one} y {number_two}, ahora Python nos dirá cuál de los dos números es mayor o si son iguales.")

if number_one > number_two:
    print(f"Es mayor {number_one}")
elif number_two > number_one:
    print(f"Es mayor {number_two}")
elif number_one == number_one:
    print("Los números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

option_one, option_two, operation = input("\nVamos a calcular con Python, introduce dos números y una operación (+, -, *, /)\n").split()
result = 0

if operation == "+":
    result = int(option_one) + int(option_two)
elif operation == "-":
    result = int(option_one) - int(option_two)
elif operation == "*":
    result = int(option_one) * int(option_two)
elif operation == "/":
    if option_two == "0":
        print("Operación no válida")
    else:
        result = int(option_one) / int(option_two)


print(f"Has elegido {option_one} y {option_two} y la operación {operation}, entonces el resultado es {result}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = input("\nIntroduce un año para saber si es bisiesto o no\n")
year_int = int(year)

if year_int %400 == 0:
    print(f"Has elegido el año {year} y es bisiesto")
elif year_int %100 == 0:
    print(f"Has elegido el año {year} y no es bisiesto")
elif year_int %4 == 0:
    print(f"Has elegido el año {year} y es bisiesto")
else:
    print(f"Has elegido el año {year} y no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = input("\nEscribe una edad cualquiera para clasificarla\n")
int_edad = int(edad)

if int_edad >= 65:
    print("Se considera adulto mayor")
elif int_edad >= 18 and int_edad <= 64:
    print("Se considera adulto")
elif int_edad >= 13 and int_edad <= 17:
    print("Se considera adolescente")
elif int_edad >= 3 and int_edad <= 12:
    print("Se considera niño")
else:
    print("Se considera bebé")