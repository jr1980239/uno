#OPERACIONES CON CADENAS DE CARACTERES

datos = "usuario\contraseña\correo"
datos = "fmalo\\123456\\fmalo@espol.edu.ec"
print(datos)
print(len(datos))

print("total de back-slash:", datos.count("\\"))

usuario = datos[:datos.find("\\")]
print(usuario)

inicio = datos.find("\\") + 1
posi = datos.find("\\", inicio)
correo = datos[posi + 1:]
print(correo)