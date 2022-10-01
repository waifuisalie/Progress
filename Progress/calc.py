def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y


print("Selecione uma operação:")
print("1.Soma")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")

while True:
    escolha = input("Escolha a opção(1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", soma(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))
        
        proxima_op = input("Fazer outra operação? (sim/nao) ")
        if proxima_op == "nao":
          break
    
    else:
        print("Invalid Input")