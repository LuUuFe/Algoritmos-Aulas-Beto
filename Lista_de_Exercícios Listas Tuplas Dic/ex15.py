# 15. (Jogo de Adivinhação) Implemente um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o usuário deve adivinhar. Após cada tentativa, diga se o número é maior ou menor que o número secreto, e conte o número de tentativas até acertar.

from random import randint

print('######################## JOGO DE ADIVINHAÇÃO ########################')

def initialization():
  secretNumber = randint(1, 100)
  attempts = 3
  while attempts > 0:
    print(f'Você possui {attempts} tentativas')
    inputNumber = int(input('Digite um número: '))
    if inputNumber == secretNumber:
      return print('Você ganhou!')
    else:
      attempts -= 1
      print('Você errou!')
      if inputNumber < secretNumber:
        print('O número digitado é menor do que o número secreto!')
      else:
        print('O número digitado é maior do que o número secreto!')
        
  if attempts == 0:
    return print('Você perdeu!')

initialization()