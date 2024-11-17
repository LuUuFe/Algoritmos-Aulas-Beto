# 10. (Calculadora de Área de Retângulo) Receba a base e a altura de um retângulo e exiba a área dele usando a fórmula

base = int(input('Digite a base do retângulo: '))
height = int(input('Digite a altura do retângulo: '))

def calculator_rectangle_area(base, height):
  return (base * height)

print(f'A área do retângulo é igual a {calculator_rectangle_area(base, height)}')