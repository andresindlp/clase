class Animal:
    def __init__(self, especie, edad, dueno):
        self.especie = especie
        self.edad = edad
        self.dueno = dueno
        print("Soy un Animal del tipo", type(self).__name__)


class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
    

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")
    def picar(self):
        print("Picar!")

mi_perro = Perro('mamífero', 7, 'Luis')
mi_perro.especie
mi_perro.edad
print("Mi dueño es", mi_perro.dueno)
