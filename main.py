
class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def fazer_som(self):
        pass
    
    def apresentar(self):
        print(f"Olá, meu nome é {self._nome} e tenho {self._idade} anos.")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")
    
    def buscar(self, objeto):
        print(f"{self._nome} está buscando o(a) {objeto}.")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")
    
    def arranhar(self, objeto):
        print(f"{self._nome} está arranhando o(a) {objeto}.")

# Criando uma função que utiliza polimorfismo
def fazer_som(animal):
    animal.fazer_som()

# Criando objetos e chamando os métodos
cachorro1 = Cachorro("Rex", 5)
gato1 = Gato("Garfield", 3)

fazer_som(cachorro1)  # Output: Au au!
fazer_som(gato1)  # Output: Miau!
