nota = float(input('Digite sua nota:'))
if nota < 0 or nota > 10:
    print('Nota inválida!!!')
else: 
    if nota < 4:
        print ('Reprovado por ',nota)
    else:
        if nota >= 7:
            print ('Aprovado por nota ',nota)
        else:
            print ('Em exame por ',nota)