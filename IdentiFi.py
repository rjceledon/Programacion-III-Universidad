# Diseñado por Ing. Ricardo Celedon
# Mcbo, 13/11/21

verNumb='0.1a' # Numero de version en variable para facil actualizacion
partnersList = [] # Lista vacia donde se guardaran los datos de nombres y cedula

def get_id(*args): # Usando *args para importar cualquier cantidad de datos
    id = str(args[0]) + str((len(args[(len(args) - 2)]))) + str(args[len(args) - 1])[0:3]
    """
    Esta linea concatena el primer argumento pasado (posicion de 1er nombre)
    luego obtiene la longitud del penultimo argumento (posicion del apellido) con len(args[(len(args) - 2)])
    y finalmente obtiene los 3 primeros digitos del ultimo argumento (posicion de la cedula) con args[len(args) - 1]
    """
    return id # Devuelve el id formateado con 1er nombre, longitud del apellido, y 3 digitos de cedula


# Programa principal
print('Bienvenido a IdentiFi v' + verNumb + '!\n') # Mensaje bienvenida

while True: # Ciclo del programa principal
    nameInput = input("Ingrese Nombres y un solo Apellido separados por espacios (en blanco para finalizar): ").strip() # Se añade .strip() para eliminar cualquier espacio en blanco al inicio
    if len(nameInput.split(' ')) > 1: # usa la funcion split para dividir datos separados por espacio en blanco, y mide la cantidad de datos
        while True:
            dniInput = input("Ahora ingrese su numero de cedula: ").strip() # Usando .strip() para evitar falsos valores en blanco
            if len(dniInput) == 7 or len(dniInput) == 8: # Evalua si la cedula tiene 7 u 8 digitos
                partnersList.append(nameInput.split(' ')) # Adjunta los nombres separados por espacio en blanco
                partnersList[len(partnersList)-1].append(dniInput) # En la misma posicion de lista, adjunta la cedula como ultimo valor
                # La lista queda [[nombre1, nombre2, ....., cedula], [otros datos]]
                print('') # Linea en blanco de estetica
                break
            else:
                print('[!] ERROR: Cedula invalida, asegurese de tener entre 7 u 8 digitos...')
    elif nameInput == '':
        if len(partnersList) > 0: # Si al menos 1 dato fue guardado
            print('')
            for i in range(0, len(partnersList)): # Itera la cantidad de entradas guardadas en la lista (2do orden)
                print('[*] ID de', partnersList[i][0], partnersList[i][int(len(partnersList[i])-2)] + ':', get_id(*partnersList[i]))
                # Imprime el nombre, apellido (posicion -2) y usa la funcion get_id, se pasa el argumento usando * para expandir y no pasar la lista, sino valores
        else:
            print('[!] ERROR: No se ha ingresado ningun dato, finalizando ejecucion...')
        break
    else:
        print('[!] ERROR: Introduzca al menos un nombre con su apellido...')

print('\n\nGracias por usar IdentiFi v' + verNumb + '!') # Mensaje de cierre
