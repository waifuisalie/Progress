cat1 = float(input('Colocar valor do cateto 1: '))   
cat2 = float(input('colocar valor do cateto 2: '))
valor = hip = (cat1**2+cat2)**(1/2)
while cat1 <= 0:
    cat1 = float(input('colocar valor do cateto 1: '))
while cat2 <= 0:
    cat2 = float(input('colocar valor do cateto 2: '))
    while cat1 and cat2 > 0:
        hip = (cat1**2+cat2)**(1/2)
print('hip:',(valor))
