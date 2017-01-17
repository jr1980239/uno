"""
mis_datos = [

    "Nombre: Frank Malo\n",
    "Edad: 30\n",
    "Cedula: 0999999",
]

f = open("L:\mis_datos.txt", "w")
f.writelines(mis_datos)
f.close()

###########################################################################
f = open("L:\\mis_datos.txt", "w")
op = -1
while op != 0:
    linea = input("Ingrese la linea")
    f.write(linea + "\n")
    op = int(input("Ingrese la opcion"))
f.close()
###########################################################################

f = open("mis_datos.txt", "r")
for linea in f:
    print(linea, end="")
f.close()


f = open("mis_datos.txt", "r")
lineas= f.readlines()
for linea in lineas:
    print(linea, end="")
f.close()

"""

