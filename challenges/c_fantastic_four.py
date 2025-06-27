# ¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

# En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

# Reed Richards (Mr. Fantastic), representado por la letra R.
# Johnny Storm (La Antorcha Humana), representado por la letra J.

# Objetivo:

# Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

# - Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
# - Si las cantidades no son iguales, la función debe retornar False.
# - En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.

# cantidad de r y j son iguales, devuelve true
# cantidad diferente, devuelve false
# cantidad 0 se considera igual

violeta_song = "Dime que soy tu castigo, por eso hace rato que te porta' mal, dime que soy tu delirio, por eso te saco tu lado animal, ponte arriba que hay trabajo, vamo' a sudar si te miro desde abajo, te va a gustar"

def how_many_j_r(violeta_song):
    words_song = violeta_song.split()
    how_many_j = 0
    how_many_r = 0

    for word in words_song:
        if 'j' in word:
            how_many_j += 1
        if 'r' in word:
            how_many_r += 1

    if how_many_r == how_many_j:
        return f"Tenemos este número de R: {how_many_r}, y este número de J: {how_many_j}, así que es true"
    else:
        return f"Tenemos este número de R: {how_many_r}, y este número de J: {how_many_j}, así que es false"

print(how_many_j_r(violeta_song))