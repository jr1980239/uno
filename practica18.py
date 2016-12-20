# Lista con las palabras a buscar
lista = ['que', 'mierda']

# Crea un diccionario partiendo de la lista. Esto lo hace consumir más memoria pero más rápido
dict = {}
for item in lista:
    dict[item] = True

# El archivo en el que vamos a buscar las palabras de la lista
f = open('kk.dat', 'r')

for line in f:
    # spliteamos la linea en palabras por espacios
    for w in line.split():
        # buscamos cada palabra en el diccionario
        if w in dict:
            print('Word is in list: ' + w)
# al terminar cerramos el archivo
f.close()