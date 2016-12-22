#DICCIONARIOS

d = {1:"test", 1.1:[5,7,"otro test"], "tercer":"otra cadena", (1,0):5}
"""
print(d[1])
print(d[1.1])
print(d["tercer"])
print(d[1,0])
print(d[1,1])
print(d[5:4])

"""

d[3]="Nuevo elemento"
d[1]="Reemplazo de valor"
print(d)