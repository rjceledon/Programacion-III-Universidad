# Ricardo Celedon C.I.:V24361484
print("Hola bienvenido a su identificador de vocales!\n")

a = input("Por favor ingrese una letra: ")
a = str(a) # Forzamos a que sea string

if len(a) > 1: # Funcion len devuelve longitud
    print("\n*ERROR* No se pudo procesar el dato.")
else: # Si es valido
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        print("\nEs una vocal!")
    else:
        print("\nEs cualquier letra, no vocal")
    
print("\n\nGracias por usar su identificador!")
