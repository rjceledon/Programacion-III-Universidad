# Diseñado por Ing. Ricardo Celedon
# Mcbo, 11/11/21

verNumb='0.1a' # Numero de version en variable para facil actualizacion

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


# Programa principal
print('Bienvenido a Num-Count v' + verNumb + '!\n') # Mensaje bienvenida

while True:
    usrInput = input("Por favor ingrese un numero entero: ")
    if valid_number(usrInput): # Evalua si return True o False
        break
    else:
        print('[!] ERROR: Asegurese de introducir un numero entero...')

print('') # Salto de linea

while True:
    digitInput = input("Ingrese ahora por favor un digito entero: ")
    if digitInput.isdigit() and len(digitInput) == 1: # Evalua que sea digito, y que su longitud sea 1
        break
    else:
        print('[!] ERROR: Introduzca solo un digito entero...')

freq = count_freq(abs(int(usrInput)), digitInput) # Obteniendo frecuencia
print('\nLa frecuencia del digito', digitInput, 'en', usrInput, 'es de', freq) # Valor
print('\n\nGracias por usar Num-Count v' + verNumb + '!') # Mensaje de cierre
