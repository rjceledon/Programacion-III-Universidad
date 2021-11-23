# Diseñado por Ing. Ricardo Celedon
# Mcbo, 11/11/21
import re # Modulo importado para usar expresiones regulares y chequear a partir de ellas

verNumb='0.1a' # Numero de version en variable para facil actualizacion
regex = '[^@]+@[^@]+\.[^@]+' # Expresion regular que busca cualquier alfanumero X@X.X
# [^@]+ -> Cualquier alfanumerico
# \. -> Escape de caracter especial

def valid_email(eMail): # Funcion para validar eMail pasando el argumento del correo
    if re.search(regex, eMail): # re.search busca el patron en el texto dado
        return True
    else:
        return False


# Programa principal
print('Bienvenido a U-Mail v' + verNumb + '!\n\nIngreso:\n') # Mensaje bienvenida
while True: # Ciclo infinito hasta que la validacion rompa el ciclo
    ingress_eMail = input('Ingrese su direccion de correo: ')
    if valid_email(ingress_eMail): # Llama a la funcion y se usa como argumento del if
        break # Sale del ciclo infinito
    else:
        print('[!] ERROR: Direccion de correo no valida...') # Mensaje de error y vuelve a empezar

print('\nHa ingresado sesion con su correo', ingress_eMail) # Indica correo valido
print('\n\nGracias por usar U-Mail v' + verNumb + '!') # Mensaje de cierre