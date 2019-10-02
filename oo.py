
class Pessoa:
    nome = ''
    idade = 0
    def __init__(self, nome, idade):
        self.nome = nome;
        self.idade = idade;
    def comer(self, comida):
        print('Comendo ' + comida)
    
    
class Estudante(Pessoa):
    curso = ''
    def __init__(self, curso, nome, idade):
        super().__init__(nome, idade)
        self.curso = curso
    def comer(self, comida):
        print('Estou no RU')
        super().comer(comida)
    def printandinho(self):
        print(self.nome + "\n" + str(self.idade) + "\n" + self.curso + "\n")
            
def main():
    
    zeze = Pessoa("zeze", 21)
    
    zeze = Estudante("Civil", zeze.nome, zeze.idade)
    
    zeze.comer("Lasanha")
    
    zeze.printandinho()

main()
