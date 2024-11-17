# 25. (Filtro de Números Pares em uma Lista) Receba uma lista de inteiros e filtre apenas os números pares.

numbers = list(range(1, 100))

parsNumbers = list(filter(lambda x: x % 2 == 0, numbers))

print(parsNumbers)