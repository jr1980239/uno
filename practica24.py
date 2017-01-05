#FUNCIONES
"""
def suma(a, b):
    return a + b

def imprimir_resultado(valor):
    print("El resultado es:", valor)

x = 5
y = 15

imprimir_resultado(suma(x,y))


def suma(a, b):
    return a + b

def imprimir_resultado(valor=""):
    if not valor:
        print("No hay resultado")
    else:
        print("El resultado es:", valor)

x = 5
y = -15

imprimir_resultado(suma(a=y, b=x))
imprimir_resultado()

"""
#
#def suma(a, b):
#    return a + b

#def resta(a, b):
#    return a - b

#def multiplicacion(a, b):
#    return a * b

#def operacion(f, a, b):
#    return f(a, b)
#x, y =(10,-15)
#print("Resultado 1", operacion(suma,x, y))
#print("Resultado 2", operacion(resta,x, y))
#print("Resultado 3", operacion(multiplicacion,x, y))

"""
def validacion_cedula(func):
    def envoltura(cedula):
        if cedula[0]=="0":
            return func(cedula)
        else:
            print("cedula no valida")
            return None
    return envoltura

@validacion_cedula  #es un decorador para que siempre este buscando antes de ingresar a la otra funcion
def ingresar_cedula(cedula):
    print("Cedula ingresada: ", cedula)


ingresar_cedula("1915578751")


# *args empaqueta los que no se les ha asignado un nombre los convierte en tuplas y
# **kwargs los conviete en diccionarios.
def miFuncion(*args, **kwargs):
    print(args)
    print(kwargs)

miFuncion(1,2,3,a =1,b=2)
"""

def suma(*args):
    total = 0
    for i in args:
        total += i
    return total


def operacion(f, *args):
    return f(*args)

print("Resultado 1", operacion(suma, 1,6,5,8,9,25,3,2,4,8))


