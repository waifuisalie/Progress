print('Verificação de Números Primos:')
n = int(input('forneça o número: '))
while n<=0:
    print ('Erro')
    n = int(input('Forneça um número diferente de 0: '))
cont = 0
i = 1
while i <= n:
    if n%i == 0:
        cont = cont+1
    i = i+1
if cont == 2:
    print (n, 'é primo')
else:
    print (n, 'não é primo')