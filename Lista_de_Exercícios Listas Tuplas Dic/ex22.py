# 22. (Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de vogais e consoantes. Ignore espaços e caracteres especiais.

import re

phrase = input('Digite uma frase: ').lower()

countConsonant = len(re.findall('[b-df-hj-np-tv-z]', phrase))
countVowel = len(re.findall('[aeiouáàâãéèêíìîóòôõúùû]', phrase))

print(f'A frase possui {countConsonant} consoantes e {countVowel} vogais.')

# Professor eu já sei programar e lembrei do uso das expressões regulares, lógico, não sei de cabeça a expressão regular para consoantes e vogais muito menos em Python então tive que pesquisar