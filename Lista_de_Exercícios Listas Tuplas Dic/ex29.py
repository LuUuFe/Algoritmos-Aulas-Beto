# 29. (Remoção de Elementos Duplicados de uma Lista Aninhada) Receba uma lista de listas (uma lista aninhada) com valores duplicados e crie uma nova lista de listas onde cada sublista contenha apenas valores únicos.

listNumbers = [
  [1, 2, 2, 3, 4, 4],
  [5, 6, 6, 7, 8, 8],
  [9, 10, 10, 11, 12, 12],
  [13, 13, 14, 15, 15, 16]
]

listNumbersDuplicatesRemoved = []

for row in listNumbers:
  listNumbersDuplicatesRemoved.append(list(set(row)))

print(listNumbersDuplicatesRemoved)