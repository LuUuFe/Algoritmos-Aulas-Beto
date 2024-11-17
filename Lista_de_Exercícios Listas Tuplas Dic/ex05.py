# 5. (Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10).

num = int(input('Digite um número para gerar tabuada: '))

for i in range(11):
  print(f'{num} * {i} = {num * i}')