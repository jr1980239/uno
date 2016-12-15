

#cadena="Eva usaba rimel y le miraba suave"

""""
frase = input('Ingrese una frase:')

temp = frase.replace(' ', '')
mi = frase.lower()
temp = mi.replace(' ', '')
if temp == temp[::-1]:
    print('La frase es palindromo')
else:
    print('No es palindromo')

    import re

patron = "^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \?=.-]*)*\/?$"
valor = "http://www.google.com.ec"

if re.match(patron, valor):
    print ("Dirección Web valida")
else:
    print("Dirección Web no valida")



################################################################################
CLASE HECHA POR EL PROFESOR.

patron = "^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
valor = "255.168.1.1"

if re.match(patron, valor):
    print ("Dirección ip valida")
else:
    print("Dirección ip no valida")


################################################################################


patron = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$"
valor = "fmalo@espol@edu.ec"

if re.match(patron, valor):
    print ("Dirección mail valida")
else:
    print("Dirección mail no valida")

"""
##########################################################################################
# Expresión regular

# Libreria para las expresiones regulares

import re

patron="^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
valor = "wwwwww.google.com.ec"

if re.match(patron, valor):
    print ("Dirección web válida")
else :
    print("Dirección web no válida")

# validar email

patron="^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$"
valor = "jr198023@gmail.com.mx"

if re.match(patron, valor):
    print ("Dirección mail válida")
else :
    print("Dirección mail no válida")


patron="^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$"
valor = "Este es mi correo jrodriguez@labhg.com.ec , este es mi correo personal jr198023@gmail.com"

if re.match(patron, valor):
    print ("Dirección mail válida")
else :
    print("Dirección mail no válida")

edad = 50;

if 10 > edad > 1 :
    print ("Niñez")
elif 18 > edad > 11 :
    print("Adolescencia")
elif 65 > edad > 19:
    print("Madurez")
else :
    print("Vejez")

edad = 15
valor = edad >= 18 and "Mayor de edad" or "Menor de edad"
print(valor)