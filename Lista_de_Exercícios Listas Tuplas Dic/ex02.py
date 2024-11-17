# 2. (Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar.

num = int(input('Digite um número: '))

if (num % 2 == 0):
  print('O número digitado é par')
else:
  print('O número digitado é ímpar')