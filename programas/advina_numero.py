# Imprimir el borde superior
print("")
print("""
#####################################################################################
#                                                                                   #
#     █████  ██████  ██ ██    ██ ██ ███    ██  █████  ███    ██ ███████  █████      #
#    ██   ██ ██   ██ ██ ██    ██ ██ ████   ██ ██   ██ ████   ██    ███  ██   ██     #
#    ███████ ██   ██ ██ ██    ██ ██ ██ ██  ██ ███████ ██ ██  ██   ███   ███████     #
#    ██   ██ ██   ██ ██  ██  ██  ██ ██  ██ ██ ██   ██ ██  ██ ██  ███    ██   ██     #
#    ██   ██ ██████  ██   ████   ██ ██   ████ ██   ██ ██   ████ ███████ ██   ██     #
#                                                                                   #
#####################################################################################
""")

print("#"*80)

print("######                                                                    ######")
print("######                 Bienvenido a ADIVINE UN NÚMERO                     ###### ")
print("######                                                                    ######")
print("######    Tendrá 3 oportunidades para adivinar el numero que pense 🧐🚀   ######")
print("######                                                                    ######")
print("######                                                                    ######")
print("#"*80)
print("")

import msvcrt
print("Presione una tecla para continuar...")# Esperar a que el usuario presione una tecla
msvcrt.getch()
# Limpiar la pantalla

import random
numero_aleatorio = random.randint(1, 10)
#print(f"Numero aleatorio entre 1 y 10: {numero_aleatorio}") #Solo lo habilito para probar
oportunidades = 1
continuar =True
num_usr = input("Que numero eligio la compu entre el 1 y el 10 ? : ")
if num_usr.isdigit() :
    num_usr=int(num_usr)
    if not num_usr <= 10 and num_usr >= 1: # RESTRICCION DEL (1,10)
        print("Solo ingresar numeros del 1 al 10")
        exit()
elif num_usr.isalpha():
    print("Solo ingresar numeros del 1 al 10")
    exit()

num_usr=int(num_usr)
frio_caliente = abs(numero_aleatorio-num_usr) #saca la cuenta en nro absoluto de la diferencia para despues comprobar si es menor de 2 es Caliente y si es menor es frio

if num_usr == numero_aleatorio : #Primer comprobacion
    continuar = False
if continuar ==True :
    if frio_caliente >= 3:
        print("No es ese, esta Frio")
    else:
        print("Esta caliente")
    num_usr= input("Ingresa otro, SEGUNDA OPORTUNIDAD : ")
    if num_usr.isdigit() :
        num_usr=int(num_usr)
        if not num_usr <= 10 and num_usr >= 1: # RESTRICCION DEL (1,10)
            print("Solo ingresar numeros del 1 al 10")
            exit()
    elif num_usr.isalpha():
        print("Solo ingresar numeros del 1 al 10")
        exit()
    oportunidades += 1 #Acumula los intentos
    num_usr=int(num_usr)
    frio_caliente = abs(numero_aleatorio-num_usr)

if num_usr == numero_aleatorio : #Segunda comprobacion
    continuar=False
if continuar == True:
    if frio_caliente >= 3 :
        print("No es ese, esta Frio")
    else:
        print("Caliente caliente....")
    num_usr= input("Arriesga otro numero, ULTIMA OPORTUNIDAD!!! : ")
    if num_usr.isdigit() :
        num_usr=int(num_usr)
        if not num_usr <= 10 and num_usr >= 1: # RESTRICCION DEL (1,10)
            print("Solo ingresar numeros del 1 al 10")
            exit()
    elif num_usr.isalpha():
        print("Solo ingresar numeros del 1 al 10")
        exit()
    num_usr=int(num_usr)
    oportunidades +=1  #Acumula los intentos

if num_usr == numero_aleatorio : #Tercer comprobacion
    print(f"Muy bien felicitado, la pegaste! El numero era el numero {numero_aleatorio} acertaste en el {oportunidades}° intento!  " )
else:
    print("Lo siento PERDISTE")
    print(f"El numero era : {numero_aleatorio}l")