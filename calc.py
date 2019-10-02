



class Calculadora:
    tela = 0
    operacao = ''
    cont = 0
    
    def somar(self, *args):
        if (self.cont == 0) :
            result = args[0] + args[1]
            self.tela += result
            self.cont = -1
            return self.tela
        else:
            result = args[0]
            self.tela += result
            return self.tela
    def subtrair(self, num1, num2):
        result = num1 + num2
        self.tela += result
        return result
    
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
    
    calc = Calculadora()
    
    a = int(input())
    b = int(input())
    print(calc.somar(a, b))
    
    print(calc.somar(int(input())))
    print(calc.somar(int(input())))
    print(calc.somar(int(input())))
    
main()
