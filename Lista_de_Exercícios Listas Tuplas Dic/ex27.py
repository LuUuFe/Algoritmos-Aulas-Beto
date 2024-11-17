# 27. (Contador de Palavras Frequentes) Peça ao usuário um texto longo e exiba as 5 palavras mais frequentes no texto, ignorando maiúsculas e minúsculas.

from collections import Counter

text = input('Digite um texto: ').lower()

topWordInText = Counter(text.split()).most_common(5)

print(topWordInText)

# Sinceramente eu até fiz utilizando somente for, lambda, sorted, reverse e etc. Porém, utilizando most_commom para limitar e Counter como um cálculo da MODA (Estatistica) é melhor viu