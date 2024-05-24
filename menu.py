import os
import operadores

operando_1 = "A"
operando_2 = "B"

resultados_listos = False


while True:
    print(f"1. Ingresar primer operando  ({operando_1})")
    print(f"2. Ingresar segundo operando ({operando_2})")
    print("3. Calcular todas las operaciones:")
    print("4. Informar resultados")
    print("5. Salir")
    
    opcion_elegida = input("Elija una opcion: ")
    
    match opcion_elegida:
        case "1":
            operando_1_listo = False
            operando_1 = input("Escriba un numero: ")
            while not operando_1_listo:
                try:
                    operando_1 = int(operando_1)
                    operando_1_listo = True
                except ValueError:
                    operando_1 = "A"
                    print("No se ha ingresado un numero valido")
                    operando_1 = input("Escriba un numero valido: ")

        case "2":
            operando_2_listo = False
            operando_2 = input("Escriba un numero: ")
            while not operando_2_listo:
                try:
                    operando_2 = int(operando_2)
                    operando_2_listo = True
                except ValueError:
                    operando_2 = "B"
                    print("No se ha ingresado un numero valido")
                    operando_2 = input("Escriba un numero valido: ")
                

        case "3":
            if operando_1_listo and operando_2_listo:
                suma = operadores.sumar(operando_1, operando_2)
                resta = operadores.restar(operando_1, operando_2)
                producto = operadores.multiplicar(operando_1, operando_2)
                try:
                    cociente = operadores.dividir(operando_1, operando_2)
                except ZeroDivisionError:
                    cociente = None
                factorial1 = operadores.factorial(operando_1)
                factorial2 = operadores.factorial(operando_2)

                print("Operaciones calculadas, informe disponible")

                resultados_listos = True
            else:
                print("Imposible calcular resultados, falta definir operandos")

            input("Presione enter para continuar")

        case "4":
            if resultados_listos:
                print(f"El resultado de {operando_1} + {operando_2} es {suma}")
                print(f"El resultado de {operando_1} - {operando_2} es {resta}")
                print(f"El resultado de {operando_1} * {operando_2} es {producto}")
                if cociente == None:
                    print("Se intentó dividir por cero, no se obtuvó un cociente")
                else:
                    print(f"El resultado de {operando_1} / {operando_2} es {cociente}")
                print(f"El resultado de {operando_1}! es {factorial1}")
                print(f"El resultado de {operando_2}! es {factorial2}")
            else:
                print("Primero se deben calcular los resultados")
            input("Presione enter para continuar")

        case "5":
            print("Adios")
            break

        case _:
            print("Para elegir una opcion valida, ingrese un numero del 1 al 5")
            input("Presione enter para continuar")

    os.system("cls")
