# 24. (Verificação de Anagrama) Receba duas palavras e determine se elas são anagramas (ou seja, possuem as mesmas letras em qualquer ordem).

word1 = input('Digite uma palavra: ').lower()
word2 = input('Digite outra palavra: ').lower()

def is_anagrams(word1, word2):
  if len(word1) != len(word2):
    return False
  for i in range(len(word1)):
    if word1.count(word2[i]) == 0 or word2.count(word1[i]) == 0:
      return False
  return True

if is_anagrams(word1, word2):
  print('As palavras são anagramas!')
else:
  print('As palavras não são anagramas!')