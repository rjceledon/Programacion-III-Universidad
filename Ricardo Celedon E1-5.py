#Realizado por Ing. Ricardo Celedon
txt = input("Por favor ingrese algun texto: ")
print("La primera letra del texto ingresado es:", txt[0])
indice = int(input("Ahora ingrese un numero menor a la cantidad de caracteres del texto ingresado (del 1 al " + str(len(txt)) + "): ")) - 1 #Se resta 1 ya que los indices empiezan por 0

if (indice <= len(txt)):
	print("El caracter #" + str(indice + 1) + " es:", txt[indice])
else:
	print("ERROR: Indice no valido.")