import funciones_capo as fc

#Ejercicio: Crear una clase de Cuenta Bancaria
#Objetivo: Implementar una clase CuentaBancaria que permita a los usuarios realizar operaciones bancarias básicas como depositar, retirar y consultar el saldo.

class CuentaBancaria:
    def __init__ (self, saldo:int | None = 0, titular : str | None = "Usuario fantasma") -> None:
        self.saldo = saldo
        self.titular = titular
        pass
    def ingresar_dinero(self) -> int :
        """Devuelve el ingreso de dinero"""
        ingreso_dinero = fc.ingresar_numero ("Ingrese la cantidad a ingresar: ")
        self.saldo = self.saldo + ingreso_dinero
        self.consulta_saldo()
        return ingreso_dinero

    def retiro_dinero(self) -> int :
        retiro_dinero = fc.ingresar_numero ("Ingrese el monto a retirar: ")
        self.saldo = self.saldo - retiro_dinero
        if self.saldo < 0:
            print(f"{self.titular} se quedo sin dinero")
            self.saldo = 0
            pass
        self.consulta_saldo()
        return retiro_dinero

    def consulta_saldo(self):
        print(f"{self.titular} su saldo es : {self.saldo}")

titular = fc.validar_texto("Ingrese su nombre : ")
saldo = fc.ingresar_numero("Ingrese su saldo actual : ")
prueba = CuentaBancaria(saldo, titular)

while True:
    nro_operacion = fc.ingresar_numero (" - 1: Depositar\n - 2: Retirar\n - 3: Consultar saldo\n - 4: Salir \n Opcion : ")
    if nro_operacion == 1:
        prueba.ingresar_dinero()
    elif nro_operacion == 2:
        prueba.retiro_dinero()
    elif nro_operacion == 3:
        prueba.consulta_saldo()
    else:
        fc.hablar(f"Gracias por usar nuestros servicios {titular} !")
        exit()

