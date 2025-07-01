# Regex son expresiones regulares y sirven para hacer una búsqueda que forma un patrón.
import re

song = """Si mi corazón de acero hoy se cierra
Diles que un día yo estuve plena
De tu amor que aún me falta
Del que no tiene mi alma

Que cruel final
Nunca podré olvidar
Lo que tuvimos
Ya no está
Tu rosa se ha marchitado


Cuento toda' las vece' que dijiste
Que me he quedado pegada a tu' cicatrice'
Cuento la' mirada' que ante' lanzamo'
Y ahora me viste la soledad


Siempre he pensado que te necesito
Y ahora tu ausencia marca mi camino
Di lo que quiera' pero esto está escrito
Dime un "te quiero" en este suspiro
En este suspiro
You might also like


Adió' recuerdos que
Aún viven en mi piel
Dime que no morirán
Aunque este sea el final


Cuento toda' las vece' que dijiste
Que me he quedado pegada a tu' cicatrice'
Cuento la' mirada' que ante' lanzamo'
Y ahora me viste la soledad


Siempre he pensado que te necesito
Y ahora tu ausencia marca mi camino
Di lo que quieras pero esto está escrito
Dime un "te quiero" en este suspiro
En este suspiro

Si mi corazón de aceto hoy se cierra
Diles que un día yo estuve plena
De tu amor que aún me falta
Del que no tiene mi alma"""

#El punto es para buscar la palabra aunque tenga otro caracter que no sea r en este caso

pattern = "ace.o"

coincidencias = re.search(pattern, song)

# Para buscar la primera coincidencia y su posición

if coincidencias:
    print(f"El patrón '{pattern}' ha sido encontrado.")
else:
    print("No hay patrón")

print("La posición de la primera coincidencia es", coincidencias.start(), coincidencias.end())

# Para buscar todas las coincidencias

coincidencias = re.findall(pattern, song)

print(f"El número de coincidencia es de {len(coincidencias)}.")

# Para iterar sobre cada coincidencia

coincidencias = re.finditer(pattern, song)

for coincidencia in coincidencias:
    print(f"Se encontró {coincidencia.group()} en la posición desde {coincidencia.start()} a {coincidencia.end()}.")