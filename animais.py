class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
     print('Nhom nhom', self.nome)

class Gato(Animal):
    def __init__(self, nome, dono, raca):
        super().__init__(nome, dono)
        self.raca = raca
      
    def miar(self):
        print('Minhauuuu')

class Cachorro(Animal):
    def latir(self):
        
        print('Au auuu')

gato = Gato('xuxuzinho', 'Mateus', 'siames')
cachorro = Cachorro('rex', 'Bárbara')
animal = Animal('toddy', 'gabriel')
cachorro.latir()

print(cachorro.nome)
print(cachorro.dono)