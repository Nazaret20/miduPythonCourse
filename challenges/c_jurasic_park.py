# En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

# Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

# Objetivo:
# Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).

nests = [12, 7, 24, 5, 18, 3, 42, 11, 8, 27, 36, 9, 2]

def dinosaur_eggs(nests):
    total_nest = len(nests)
    total_eggs_in_nests = 0

    for total_eggs in nests:
        total_eggs_in_nests += total_eggs

    carnivorous_eggs = 0
    total_carnivorous_nest = 0
    
    for nest in nests:
        if nest % 2 == 0:
            carnivorous_eggs += nest
            total_carnivorous_nest += 1

    return f"🦖🥚 En total se han encontrado una cantidad de {total_nest} nidos, que a su vez el total de huevos han sido {total_eggs_in_nests}, pero siendo de carnívoros el total de huevos han sido {carnivorous_eggs} en un total de {total_carnivorous_nest} nidos."

print(dinosaur_eggs(nests))