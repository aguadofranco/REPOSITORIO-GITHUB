import random

palabras = ["manzana", "banana", "pera", "uva", "naranja"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []

def nombre_jugador(jugador:str | None=True):
    jugador = input ("Ingresa tu nombre para comenzar: ")
    if jugador == "":
        jugador = "Jugador Anonimo"
    print(f"¡Bienvenido {jugador} al juego del ahorcado!")
    return jugador

def corroborar_palabra():
    intentos = 6
    while intentos > 0:
        palabra_actual = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_actual += letra
            else:
                palabra_actual += "_"
        print("Palabra:", palabra_actual)
        if palabra_secreta == palabra_actual:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break
        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Has perdido! La palabra era:", palabra_secreta)
        puntos = 0
    if intentos >= 5 :
        puntos = 20
        print (f"Su puntaje es {puntos} puntos")
    elif intentos >= 3 :
        puntos = 15
        print (f"Su puntaje es {puntos} puntos")
    elif intentos >= 0 :
        puntos = 10
        print (f"Su puntaje es {puntos} puntos")
    return palabra_actual, intentos

nombre_jugador()
corroborar_palabra()
