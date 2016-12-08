#SENTENCIAS

from datetime import datetime

anio_nacimiento = input("Ingrese su año de nacimiento: ")
#print(type(anio_nacimineto))


print(datetime.now().year - int(anio_nacimiento))

