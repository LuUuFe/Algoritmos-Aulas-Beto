# 26. (Mesclagem de Dois Dicionários) Dado dois dicionários, mescle-os em um terceiro. Caso eles tenham chaves em comum, some os valores das chaves correspondentes.

dict1 = {
  'valor1' : 10,
  'valor2' : 20
}

dict2 = {
  'valor1' : 30,
  'valor3' : 10
}

dict3 = dict1.copy()

for key in dict2:
  if key in dict3:
    dict3[key] += dict2[key]
  else:
    dict3[key] = dict2[key]

print(dict3)