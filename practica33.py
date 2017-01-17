class Persona:

    TIPO_IDENTIFICACION_CEDULA = "C"
    TIPO_IDENTIFICACION_RUC = "R"

    def _init_(self, identificacion, tipo_identificacion):
        self.identificacion = identificacion
        self.tipo_identificacion = tipo_identificacion

    def _str_(self):
        return "%s" % self.identificacion

    def imprimir_informacion(self):
        print("%s" % self.identificacion)

class PersonaNatural(Persona):
    def _init_(self, cedula, nombres, apellidos, edad):
        Persona._init_(self, cedula, Persona.TIPO_IDENTIFICACION_CEDULA)
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad

    def _str_(self):
        return "%s" % (self.nombres, self.apellidos)

    def imprimir_informacion(self):
        Persona.imprimir_informacion(self)
        print("%s" % self.nombres)
        print("%s" % self.apellidos)
        print("%s" % self.edad)

class PersonaJuridica(Persona):
    def _init_(self, ruc, razon_social):
        Persona._init_(self, ruc, Persona.TIPO_IDENTIFICACION_RUC)
        #self.ruc = ruc
        self.razon_social = razon_social

    def _str_(self):
        return "%s" % (self.razon_social)

    def imprimir_informacion(self):
        Persona.imprimir_informacion(self)
        print("%s" % self.razon_social)

pn1 = PersonaNatural("0915578751", "Jose", "Rodriguez", 36)
pn2 = PersonaNatural("0999999999", "Lorenzo", "Vinueza", 80)
pn3 = PersonaNatural("0900099909", "Frank", "Malo", 30)

pn1.imprimir_informacion()