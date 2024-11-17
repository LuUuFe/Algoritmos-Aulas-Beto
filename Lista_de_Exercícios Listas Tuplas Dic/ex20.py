# 20. (Gerador de Números da Sequência de Fibonacci) Peça ao usuário um número n e gere uma lista com os n primeiros números da sequência de Fibonacci

num = int(input('Digite um número: '))

listFibonacci = [0, 1]
while num > 2:
  listFibonacci.append(listFibonacci[-1] + listFibonacci[-2])
  num -= 1


print(listFibonacci[0]) if num == 1 else print(listFibonacci)