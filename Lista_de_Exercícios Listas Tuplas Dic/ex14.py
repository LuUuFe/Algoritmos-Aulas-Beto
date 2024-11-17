# 14. (Verificador de Palíndromos) Receba uma palavra e determine se ela é um palíndromo (ou seja, se lê igual de trás para frente).

word = input('Digite uma palavra: ').lower()

if word == word[::-1]:
  print('A palavra digitada é um palíndromo!')
else:
  print('A palavra digitada não é um palíndromo!')