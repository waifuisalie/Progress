idade = int(input('Idade: '))
if idade <= 0 :
    print('Idade inexistente!!!')
elif idade < 16:
    print('Não eleitor')
elif 18 <= idade <= 65:
    print ('Eleitor obrigatório!!!')
else:
    print('Eleitor facultativo!!!')