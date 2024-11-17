# 19. (Contador de Caracteres de uma Frase) Receba uma frase e retorne um dicionário que contém a quantidade de cada caractere (inclusive espaços).

phrase = input('Digite uma frase: ')

phraseDict = {}

for char in phrase:
  phraseDict[char] = phrase.count(char)

print(phraseDict)