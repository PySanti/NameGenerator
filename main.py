from random import randint, choice
import time
vocales     = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"
vocales     = [i for i in vocales]
consonantes = [i for i in consonantes]

def generateSilaba(letters_count):
    if letters_count == 1:
        return choice(vocales)
    elif letters_count == 2:
        return f"{choice(consonantes)}{choice(vocales)}"
    elif letters_count == 3:
        if randint(1,2) == 1:
            return f"{choice(consonantes)}{choice(vocales)}{choice(consonantes)}"
        else:
            return f"{choice(vocales)}{choice(consonantes)}{choice(vocales)}"
nombres_count = int(input("Introduce un numero -> "))
while nombres_count != 0:
    nombres_count -= 1
    silabas_count = randint(2,3)
    nombre = ""
    for silabas in range(silabas_count):
        silaba = None
        if silabas_count == 3 or (silabas_count == 2 and (len(nombre) in [2,3])):
            silaba = generateSilaba(randint(1,3))
        else:
            silaba = generateSilaba(randint(2,3))
        nombre += silaba
    print(nombre.capitalize())







