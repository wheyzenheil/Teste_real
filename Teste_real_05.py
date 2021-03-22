salario = float(input('digite o valor do salario:  '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

print('Salario antigo: R$ ', salario)
print('Percentual: ', percentual, '%')

percentual = percentual / 100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('Valor do aumento: R$ ', aumento)
print('Salário atualizado: R$ ', novo_salario)
