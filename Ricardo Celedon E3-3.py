# Diseñado por Ing. Ricardo Celedon
# Mcbo, 11/11/21
from math import sqrt

verNumb='0.1a' # Numero de version en variable para facil actualizacion
firstRunFlag = False
maxNumb = 0

def valid_number(intNumb): # Funcion para validar el numero usando un try para ver si puede convertirse a integer
    try:
        int(intNumb) # Intenta convertir a integer
        return True
    except ValueError:
        return False

def count_freq(intNumb, digit): # Funcion para contar la frecuencia del digito
    digitCount = 0 # Inicializacion a conteo 0
    for d in str(intNumb): # Iteracion de cada digito del intNumb pasandolo a str
        if (int(d) == int(digit)): # Comparando valores (se fuerzan a ser int para matchear)
            digitCount += 1 # Aumento del contador
    return digitCount # Devuelve el conteo total

def is_prime(intNumb): # Funcion para validar si el numero es primo
    if intNumb > 1:
        for i in range(2, int(sqrt(intNumb)) + 1): # Itera haciendo el modulo de intNumb de 2 hasta la sqrt del numero + 1
            if (intNumb % i) == 0: # Al hallar un numero que sea factor de el
                return False # Rompe y regresa false
        else:
            return True # Si el for termina (notese que el else es del for, y no del if) sin encontrar ningun factor, devuelve true
    else:
        return False # Si es 1 o menor, regresa false

def fact_result(intNumb): # Determina el factorial recursivamente
    if intNumb == 1 or intNumb == 0:
        return 1 # Si es 0 o 1, regresa 1 siempre
    else:
        return intNumb * fact_result(intNumb - 1) # Llamada recursiva

# Programa principal
print('Bienvenido a Num-Prime v' + verNumb + '!\n') # Mensaje bienvenida

while True:
    while True:
        usrInput = input("Ingrese solamente numeros primos: ")
        if valid_number(usrInput): # Evalua si return True o False
            break
        else:
            print('[!] ERROR: Asegurese de introducir un numero valido...')

    if not(is_prime(abs(int(usrInput)))): # Se usa abs para poder usar numeros negativos
        print('[!] Ha ingresado un numero no primo, finalizando conteo...')
        break
    else:

        while True:
            digitInput = input("Ingrese ahora por favor un digito entero: ")
            if digitInput.isdigit() and len(digitInput) == 1:  # Evalua que sea digito, y que su longitud sea 1
                break
            else:
                print('[!] ERROR: Introduzca solo un digito entero...')
        freq = count_freq(abs(int(usrInput)), digitInput)  # Obteniendo frecuencia
        print('[*]', usrInput, 'es un numero primo')
        print('[*] La frecuencia del digito', digitInput, 'en', usrInput, 'es de', freq, '\n')  # Valor

        if not firstRunFlag: # Solo si es la primera corrida
            firstRunFlag = True
            maxNumb = usrInput # Setear el valor inicial primario
        else: # Luego de la primera corrida
            if int(usrInput) > int(maxNumb): maxNumb = usrInput # Asignar el mayor

if firstRunFlag: print('\n[**] El factorial del numero maximo ingresado', maxNumb, 'es de', fact_result(abs(int(maxNumb))))



print('\n\nGracias por usar Num-Prime v' + verNumb + '!') # Mensaje de cierre