#Simulador de cajero automático:
#Desarrolla un simulador simple de cajero automático que permita al usuario realizar las siguientes operaciones:
#Consultar saldo
#Depositar dinero
#Retirar dinero
#Utiliza instrucciones if y elif para validar las opciones ingresadas por el usuario y realizar las operaciones correspondientes. Implementa un sistema de control de saldo para evitar retiros que superen el monto disponible.

def ingresar_numero (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero entero mayor a 0\n texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            if numero_1 >= 0:
                break
            else:
                print("\nEl valor ingresado debe ser mayor a 0")
        else:
            print("\nEl valor ingresado no es un Nro")
    return numero_1

saldo = 100000

while True:
    operacion = ingresar_numero ("\nIngrese que operacion quiere hacer: \n\n 1 - CONSULTA SALDO \n 2 - INGRESAR DINERO \n 3 - SACAR DINERO \n 4 - SALIR \n Opcion : ")
    operacion = str(operacion)
    if operacion == ("1") :
        print(f"\n Su saldo es: {saldo}")

    elif operacion ==("2") :
        ingreso_dinero = ingresar_numero("\n Ingrese el monto : ")
        saldo = saldo + ingreso_dinero
        print(f"\n Su dinero ingresado es {ingreso_dinero} , y su saldo actualizado es {saldo}")

    elif operacion == ("3") :
        egreso_dinero = ingresar_numero("\n Ingrese el monto a retirar : ")
        saldo = saldo - egreso_dinero
        print (f"\n Usted retira {egreso_dinero} y su saldo actualizado es: {saldo}" )

    else :
        print("\n Nos vemos, gracias por uasar nuestro servicio\n")
        False
        exit()


