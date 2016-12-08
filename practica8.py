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

print(correo.capitalize())  # la primera en mayuscula
print(correo.endswith("ec")) # cuando termine con algo que le pongamos
print(correo.startswith("fmalo")) # cuando inicia con algo que le pongamos

print(correo.islower()) # si esta toda la cadena en minusculas
print(correo.isupper()) # si esta toda la cadena en mayusculas
print(correo.upper()) # convertir toda la cadena en mayusculas
print(correo.lower()) # convertir toda la cadena en minusculas

cadena= '{:0<13}'.format('0915578751')
print(cadena)

data = "0000estos0 son0 mis0 datos1110000000"
data_limpia = data.strip("0").strip("1")  #Eliminar caracteres raros
print(data_limpia)

data_limpia = data_limpia.replace("0", " ").replace("  "," ") # remplazar los valores en las cadenas.
print(data_limpia)

print(datos.split("\\"))




