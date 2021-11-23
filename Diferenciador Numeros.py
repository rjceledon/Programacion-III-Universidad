# Ricardo Celedon C.I.:V24361484
print("Hola bienvenido a su diferenciador de numeros!\n")

a = input("Por favor ingrese un numero: ")
while(not(a.strip().isdigit())): # Usando el valor negado de .strip().isdigit() se valida si el valor es numerico
    a = input("*ERROR* Por favor ingrese un numero: ") # Repetira el mensaje hasta que sea true

print() # Salto de linea
b = input("Ingrese un segundo numero: ")
while(not(b.isdigit())):
    b = input("*ERROR* Ingrese un segundo numero: ")

print()
c = input("Ahora ingrese un tercer numero: ")
while(not(c.strip().isdigit())):
    c = input("*ERROR* Ahora ingrese un tercer numero: ")

print()
if a == b and b == c: # Todos iguales
    print("Los tres numeros son iguales!!")
elif  (a == b) or (a == c) or (b == c): # Al menos dos
    print("Dos numeros son iguales!")
else:
    print("Todos los numeros son diferentes")
    
print("\n\nGracias por usar su diferenciador!")
