### No intentes entender este código, sólo fíjate en cómo se utiliza abajo  
# Creo una estructura para los clientes
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{}: {} {}'.format(self.dni,self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

hector = Cliente("11111111A", "Hector", "Costa Guzman",)
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")
andres = Cliente("12345678Z", "Andrés", "Salan")
bill_gates = Cliente("33333333S", "Bill", "Gates")



empresa = Empresa(clientes=[hector, juan, andres])
microsoft = Empresa(clientes=[bill_gates, andres])


print("==LISTADO DE CLIENTES==")
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")
empresa.mostrar_cliente("12345678Z")
microsoft.mostrar_cliente("33333333S")
microsoft.mostrar_cliente("12345678Z")



empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")
empresa.borrar_cliente("12345678Z")


print("\n==LISTADO DE CLEIENTE==")

for i in empresa.clientes:
    print(i)