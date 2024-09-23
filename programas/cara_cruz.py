print("""
 ██████╗ █████╗ ██████╗  █████╗      ██████╗      ██████╗██████╗ ██╗   ██╗███████╗    ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗    ██╔════╝██╔══██╗██║   ██║╚══███╔╝    ╚════██╗
██║     ███████║██████╔╝███████║    ██║   ██║    ██║     ██████╔╝██║   ██║  ███╔╝       ▄███╔╝
██║     ██╔══██║██╔══██╗██╔══██║    ██║   ██║    ██║     ██╔══██╗██║   ██║ ███╔╝        ▀▀══╝
╚██████╗██║  ██║██║  ██║██║  ██║    ╚██████╔╝    ╚██████╗██║  ██║╚██████╔╝███████╗      ██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝      ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝

                                                                                              """)
print("En este juego podras elegir jugar de a 2 jugadores 👨🏾‍🤝‍👨🏼 o solo contra la PC. 🎮👨")
print()
continuar = True
de_nuevo = "Jugamos de Nuevo ??? : "
nombre_jugador1 = "ELIJIO UN JUGADOR, CONTRA LA COMPU 👾 INGRESA TU NOMBRE :"
mensaje_ganador = "Muy bien ganasteee!!!"
mensaje_perdedor = "Noooo PERDISTEEE  !!!"
#Valida si ingresa 1 o 2 y si solo ingresa digitos
jugadores = input("Ingrese la cantidad de jugadores :")
if jugadores == jugadores.isdigit():
    jugadores = int(jugadores)
while jugadores !="2" and jugadores !="1" :
    jugadores= input("Lo siento no comprendí, volve a ingresar 1 o 2?  :")

#Random para el arbitro
import random
arbitro = random.randint(1,2)
if arbitro == 1 :
    arbitro = "CARA"
if arbitro == 2 :
    arbitro = "CRUZ"
moneda= f"Tiramos la moneda y salio : {arbitro}"

#Random para eleccion de la compu
import random
eleccion_compu = random.randint(1,2)
if eleccion_compu == 1 :
    eleccion_compu = "CARA"
if eleccion_compu == 2 :
    eleccion_compu = "CRUZ"

#Eleccion 1 jugador

if jugadores == "1" :
    jugador_solo = input(nombre_jugador1)
    while continuar == True:
        jugador_solo_primero = input(f"Hola {jugador_solo}, vas a jugar contra la compu, mucha suerte!! queres elejir primero? pone SI : ")
        jugador_solo_primero = jugador_solo_primero.upper()
        if jugador_solo_primero == "SI":
            eleccion_cara_cruz=input(f"{jugador_solo}, eleji cara o cruz : ")
            eleccion_cara_cruz=eleccion_cara_cruz.upper()
            if eleccion_cara_cruz.isalpha() and eleccion_cara_cruz == "CARA" or eleccion_cara_cruz == "CRUZ" :
                if eleccion_cara_cruz == arbitro :
                    print()
                    print(moneda)
                    print(mensaje_ganador)
                    continuar=input(de_nuevo)
                    continuar=continuar.upper()
                    if continuar == "SI":
                        continuar = True
                    else:
                        continuar = False
                else:
                    print()
                    print(moneda)
                    print()
                    print(f"perdiste {jugador_solo}, salió {arbitro}")
                    print()
                    continuar=input(de_nuevo)
                    continuar=continuar.upper()
                    if continuar == "SI":
                        continuar = True
                    else:
                        continuar = False
        else :
            print()
            print(f"Ok, la compu primero, elijio {eleccion_compu}")
            print()
            eleccion_jugador_1 = "CARA"
            if eleccion_compu == "CARA":
                eleccion_jugador_1 = "CRUZ"
            print(moneda)
            if eleccion_compu == arbitro :
                print(mensaje_perdedor)
                continuar=input(de_nuevo)
                continuar=continuar.upper()
                if continuar == "SI":
                    continuar = True
                else:
                    continuar = False
            else:
                print()
                print(mensaje_ganador)
                print()
                continuar=input(de_nuevo)
                continuar=continuar.upper()
                if continuar == "SI":
                    continuar = True
                else:
                    continuar = False

# 2 JUGADORES
while jugadores == "2" and continuar :
    print()
    jugador1 = input ("Ingrese el noombre del juagador 1 : ")
    print()
    jugador2 = input ("Ingrese el nombre del jugador 2 : ")
    print()
    while continuar:
        eleccion_jugador_1 = input(f"{jugador1} elejís Cara o Cruz : ")
        eleccion_jugador_1=eleccion_jugador_1.upper()
        if eleccion_jugador_1.isalpha() and eleccion_jugador_1 == "CARA" or eleccion_jugador_1 == "CRUZ" :
            continuar=False
    eleccion_jugador_2 = "CARA"
    if eleccion_jugador_1 == "CARA":
        eleccion_jugador_2 = "CRUZ"
    print()
    print(f"{jugador2} te queda {eleccion_jugador_2}: ")
    print(moneda)
    if arbitro == eleccion_jugador_1:
        print()
        print(f"El ganador es {jugador1}")
        print()
    else:
        print()
        print(f"El ganador es {jugador2}")
        print()
    continuar_escrito=input(de_nuevo)
    continuar_escrito=continuar_escrito.upper()
    if continuar_escrito == "SI":
        continuar = True
    else:
        print("Nos Vemo !!")
        continuar = False

