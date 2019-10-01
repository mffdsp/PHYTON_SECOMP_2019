'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def mult():
    print("digita o primeiro digito, meu querido!")
    a = int(input())
    print("digita o segundo digito, meu querido!")
    b = int(input())
    return a * b;
    
def soma():
    print("digita o primeiro digito, meu querido!")
    a = int(input())
    print("digita o segundo digito, meu querido!")
    b = int(input())
    return a + b;
def sub():
    print("digita o primeiro digito, meu querido!")
    a = int(input())
    print("digita o segundo digito, meu querido!")
    b = int(input())
    return a - b;

def div():
    print("digita o primeiro digito, meu querido!")
    a = int(input())
    print("digita o segundo digito, meu querido!")
    b = int(input())
    return a / b;
    
def raiz():
    print("digita o digito, meu querido!")
    a = int(input())
    return a ** 0.5
    
def pot():
    print("digita o digito, meu querido!")
    a = int(input())
    print("digita o expoente, meu querido!")
    b = int(input())
    return a ** b;

comando = {'*' : mult, '+' : soma, '-' : sub, '/' : div, 'r' : raiz, 'p' : pot}

def main():
    while 1 == 1:
        
        print("Digita o comando ai meu querido:\n * =  multiplicação\n + =  soma\n / =  Divisão\n r =  Raiz\n p =  Potencia" )
        
        cmd = input()
        print(comando[cmd]())
main()

