# 1. (Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

def sum(num1, num2):
    return num1 + num2

print(f'A soma de {num1} + {num2} é igual a {sum(num1, num2)}')