# Ricardo Celedon C.I.:V24361484
print("Hola bienvenido a su centro de votacion!\n")

print("Los candidatos disponibles son: \n\nA por el partido rojo\nB por el partido verde\nC por el partido azul\n")

elec = input("Por favor elija el candidato de su eleccion (A/B/C): ")
elec = str(elec) # Forzamos a ser string

if elec == 'A' or elec == 'a': # Sin sensibilidad a mayusculas
    print("\nUsted ha votado por el partido Rojo!")
elif elec == 'B' or elec == 'b':
    print("\nUsted ha votado por el partido Verde!")
elif elec == 'C' or elec == 'c':
    print("\nUsted ha votado por el partido Azul!")
else:
    print("\n*ERROR* Opcion erronea")

    
print("\n\nGracias por usar su centro de votacion!")
