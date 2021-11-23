# Ricardo Celedon C.I.:V24361484
import math # Para poder usar la funcion de raiz cuadrada sqrt()

print("Hola bienvenido a su calculadora de ecuaciones cuadraticas!\n")

print("La ecuacion evaluada es la siguiente: ax^2 + bx + c = 0\n")

a = input("Por favor ingrese el coeficiente a: ")
while(not(a.strip().isdigit())): # Usando el valor negado de .strip().isdigit() se valida si el valor es numerico
    a = input("*ERROR* Por favor ingrese el coeficiente a: ") # Repetira el mensaje hasta que sea true
a = int(a) # Forzamos la variable a ser int

print() # Salto de linea
b = input("Ingrese el coeficiente b: ")
while(not(b.isdigit())):
    b = input("*ERROR* Ingrese el coeficiente b: ")
b = int(b)

print()
c = input("Ahora ingrese el coeficiente c: ")
while(not(c.strip().isdigit())):
    c = input("*ERROR* Ahora ingrese el coeficiente c: ")
c = int(c)

# La solucion de esta ecuacion es
# x = - b +- sqrt ( b ^ 2 - (4*a*c) / 2*a)  

disc = float(b**2 - (4*a*c)) # Discriminante de la ec. cuadratica

if a == 0 or disc < 0:
    print("\nLa ecuacion planteada no tiene solucion.")
elif disc == 0:
    sol1 = - (b / 2*a) # Solo 1 solucion doble
    print("\nLa solucion es", sol)
elif disc > 0:
    sol1 = (- b + math.sqrt(disc)) / 2*a # Solucion 1
    sol1 = round(sol1, 2) # Forzamos a solo tener 2 decimales
    sol2 = (- b - math.sqrt(disc)) / 2*a # Solucion 2
    sol2 = round(sol2, 2)
    print("\nLas dos soluciones posibles son " + str(sol1) + " y " + str(sol2))
    # Se convierten a str() para concatenar
    
print("\n\nGracias por usar su calculadora cuadratica!")
