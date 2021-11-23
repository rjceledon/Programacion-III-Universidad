#Realizado por Ing. Ricardo Celedon
print("Bienvenido a su calculadora de combustible para motos!")
dist = float(input("Por favor ingrese la distancia en Kilometros del recorrido: "))
comb = float(input("Ahora ingrese el combustible en litros consumido: "))
rendimiento = comb / dist
print("El combustible consumido por Kilometro fue de", rendimiento, "litros.")