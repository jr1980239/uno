#CADENAS DE CARACTERES


cadena = "Esto es un texto"

print(cadena[0])
print(cadena[6])
print(cadena[-1])

cadena = "Esto es un \" texto \" entre comillas "
print(cadena)

cadena = "una\t\ttabulación"
print(cadena)

cadena = "Primera línea\nSegunda línea"
print(cadena)

cadena = "Hola Bienvenidos\rAdios Mundo"
print(cadena)

#OPERACIONES QUE PODEMOS HACER SOBRE LAS CADENAS DE TEXTO.

cadena = "HOLA MUNDO"
print (cadena[2:7])
print (cadena[-8:-3])
print (cadena[-8:-3:2])
#print (cadena[1:7]+cadena[8:10])
print (cadena[5:])
print (cadena[:4])
print (cadena[::-1])  #-->  invertir string
print (cadena[6:1:-2]) #-->  substring invertido
print (cadena[-7:-11:-1])
print (cadena[:-6:-1])
print (cadena[-7::-1])
#####################################################################
#len para conocer el tamaño del dato o caracteres

print(len(cadena))

print(min("hola@mundo")) #presenta el caracter minimo en este caso es el @
print(max("hola@mundo")) #presenta el caracter maximo en este caso es la u
print(max("hola@mundo z")) #presenta el caracter maximo en este caso es la z





