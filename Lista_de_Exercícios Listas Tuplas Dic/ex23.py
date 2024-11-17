# 23. (Calculadora Básica com Estruturas Condicionais) Peça ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.

print('############### CALCULADORA BÁSICA ###############')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

operation = int(input('Digite o número correspondente a operação: 1 = adição, 2 = subtração, 3 = multiplicação, 4 = divisão): '))

if operation == 1:
  print(f'{num1} + {num2} = {num1 + num2}')
if operation == 2:
  print(f'{num1} - {num2} = {num1 - num2}')
if operation == 3:
  print(f'{num1} * {num2} = {num1 * num2}')
if operation == 4:
  print(f'{num1} / {num2} = {num1 / num2}')