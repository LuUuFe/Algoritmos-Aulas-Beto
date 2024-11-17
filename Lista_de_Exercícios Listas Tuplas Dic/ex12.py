# 12. (Números Primos em um Intervalo) Receba um intervalo de números do usuário (por exemplo, entre 10 e 50) e retorne uma lista com todos os números primos dentro desse intervalo.

numMin = int(input('Digite o número mínimo para o intervalo: '))
numMax = int(input('Digite o número máximo para o intervalo: '))

listPrime = []

def is_prime(num):
  if num == 1:
    return False
  for j in range(2, int(num / 2) + 1):
    if num % j == 0:
       return False
  return True

for i in range(numMin, numMax):
  if is_prime(i):
    listPrime.append(i)

print(listPrime)