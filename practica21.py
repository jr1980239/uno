#TUPLAS NO SON MUTABLES(NO CAMBIAN) -- SON CON PARENTESIS SEPARADAS CON COMAS.

opciones = (
    ("opcion 1", 1),
    ("opcion 2", 2)
  )

print(opciones[0][1])

a =  ("opcion 1", 1)
la = list(a)
la[1]=2
a=tuple(la)
print(a)