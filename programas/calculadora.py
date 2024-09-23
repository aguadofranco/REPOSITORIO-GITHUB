#Hacer un programa que me permita ingresar tres valores, siendo los primeros dos los números a utilizar y el tercero indicará la operación matemática a realizar(S, R, M, D) necesitaría que cuando me imprima el resultado tenga el siguiente formato de salida: Operación realizada con éxito, el resultado de (Aquí debe mostrar que operación se realizó) es (aquí debe mostrar el resultado) tengan en cuenta que no se puede dividir por CERO así que me debería advertir si lo coloco en el segundo número

def suma():
    resultado = valor_uno+valor_dos
    print(f"Operación realizada con éxito, el resultado de {valor_uno} + {valor_dos} = {resultado}")
    return
def resta():
    resultado = valor_uno-valor_dos
    print(f"\nOperación realizada con éxito, el resultado de {valor_uno} - {valor_dos} = {resultado}")
    return
def multiplicacion():
    resultado = valor_uno*valor_dos
    print(f"\nOperación realizada con éxito, el resultado de {valor_uno} x {valor_dos} = {resultado}")
    return
def division():
    if valor_dos == (0):
        print ("\nNo se puede dividir por 0 !")
    else:
        resultado = valor_uno/valor_dos
        print(f"\nOperación realizada con éxito, el resultado de {valor_uno} {operacion} {valor_dos} = {resultado}")
    return

while True:
    operacion = input("\nIngrese que opreacion necesita hacer: \n S - SUMA \n R - RESTA \n M - MULTIPLICACION \n D - DIVISION \n Opcion : ").upper()
    if operacion == ("S") or operacion == ("R") or operacion == ("M") or operacion == ("D") :
        valor_uno=int(input("\nIngrese el primer valor   ->  "))
        valor_dos=int(input("\nIngrese el segundo valor  ->  "))

        if operacion == ("S") :
            suma()
        elif operacion == ("R") :
            resta()
        elif operacion == ("M") :
            multiplicacion()
        elif operacion == ("D") :
            division()
        else :
            exit
    else :
        print("\nEscribiste cualquier cosa, menos una operacion")
    continuar = input ("\nPara salir ingrese Q , para continuar presione ENTER : ")
    if continuar == ("") :
        continue
    else :
        break