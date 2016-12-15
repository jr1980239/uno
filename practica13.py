# SENTENCIA FOR

#for i in range(10, 0, -1):
 #   print (i)

"""
mensaje = "Hola mundo"
for letra in mensaje:
      print (letra)

for i in range(10):
      print (i)


dato = "frank|30|fmalo@espol.edu.ec"
datos = dato.split("|")
#print(datos)

for elemento in datos:
      print (elemento)
"""

#numeros = [1,56,875,36,75,78,96,36]

#for item in numeros:
 #     print (item)

#for indice in range(len(numeros)):
 #     print(numeros[indice])

#for indice in range(len(numeros)):
#    if numeros[indice] % 2 == 0:
#     print(numeros[indice], "es par")
 #   else:
 #       print(numeros[indice], "es impar")

mensaje = "Esto es una cadena de texto".lower()
vocales = 0
consonantes = 0

conjunto_vocales = "aeiou"

for letra in mensaje:
      if letra in conjunto_vocales:
          vocales+=1
      else:
          consonantes+=1
print ("cantidad de vocales", vocales, "cantidad de consonantes", consonantes)

