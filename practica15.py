#LISTAS
"""
a = [1,2,3,4]
print (a)

a.insert(5,"test")
print(a)

elemento =  a.pop()
print(elemento)

a.remove(1)
print(a)

a.reverse()
print(a)

a.sort()
print(a)
"""
l= [ i for i in range(1,10) if i%2==0]

print(l)

lista = ["frank","Carlos","Lourdes","Ana","Mercedes","Maria","Maria Belen","Fernando"]
lista2 = [nombre.upper() for nombre in lista if nombre.lower().startswith("m")]
#lista2 = [nombre for nombre in lista if nombre.lower().startswith("m")]

print(lista2)