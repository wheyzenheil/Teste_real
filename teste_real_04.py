nota1=float(input('digita o valor da nota 1: '))
nota2=float(input('digite o valor da nota 2: '))
media=(nota1+nota2)/2
print('media alcancada:',media)
if media >= 7:
    print('Aprovado')
else:
    if media < 7:
        print('reprovado')
    else:
        if media==10:
            print('aprovado com louvor')

