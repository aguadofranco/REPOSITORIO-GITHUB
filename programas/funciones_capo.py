#Nuestas funciones

import pyttsx3


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
                print("El valor ingresado debe ser mayor a 0")
        else:
            print("El valor ingresado no es un Nro")
    return numero_1

def numero_decimal (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero mayor o menor a cero\n texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            break
        else:
            print("El valor ingresado no es un Nro")
    return numero_1


def validar_texto(texto_input:str | None="Ingrese un texto: ", validar_vacio : bool| None=False, dato_a_validar :str |None="dato")->str:
    """
    Valida si es un texto. Se puede validar que no quede el dato vacio y se puede pasar que dato valida para mostrar al usuario
    """
    while True:
        texto = input(texto_input)
        if validar_vacio:
            if texto =="":
                print (f"El {dato_a_validar} no debe quedar vacio!")
            elif texto.isalpha():
                break
            else:
                print("El dato no corresponde a lo solicitado.")
        else:
            break
    return texto



#Ejemplo 1: Una funcion que salude, teniendo en cuenta que puede tener doble nombre y doble apellido:

def saludo(nombre:str, apellido:str | None = " ")->str:
    print(f"Hola {nombre}{apellido}")
    return


# HABLA LA COMPU

def hablar(hablar:str | None = "" ):
    """Ingrese el texto de lo que quiera que repita entre los paréntesis\n si no ingresa nada no hace nada."""
    engine= pyttsx3.init()
    rate=engine.getProperty("rate")
    engine.setProperty("rate",120)
    voces = engine.getProperty("voices")
    engine.setProperty("voice", voces[1].id)
    engine.say(hablar)
    engine.runAndWait()
    return hablar
