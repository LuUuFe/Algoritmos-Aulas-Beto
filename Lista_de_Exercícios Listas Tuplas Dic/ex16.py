# 16. (Calculadora de Fatorial Recursiva) Crie uma função recursiva que calcula o fatorial de um número dado pelo usuário.

number = int(input('Digite um número: '))

# Sobre funções recursivas eu já tinha conhecimento, portanto, eu quis fazer

def factorial(num):
  if num == 0:
    return 1
  elif num > 1:
    return num * factorial(num - 1)
  else:
    return num
  
print(f'O fatorial de {number} é igual a {factorial(number)}')