# 11. (Contador de Palavras Únicas) Peça ao usuário uma frase e, em seguida, conte quantas palavras únicas ela possui (sem considerar maiúsculas e minúsculas).

phrase = input('Digite uma frase: ').lower().split()

count = 0

for word in phrase:
  if phrase.count(word) == 1:
    count += 1

print(f'A quantidade de palavras únicas são {count}')