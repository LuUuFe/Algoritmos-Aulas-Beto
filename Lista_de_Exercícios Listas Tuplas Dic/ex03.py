# 3. (Conversor de Temperatura) Receba uma temperatura em graus Celsius e converta para Fahrenheit usando a fórmula:

temp = float(input('Digite uma temperatura em graus Celsius: '))

def celsius_to_fahrenheit(temp):
  return temp * 1.8 + 32

print(f'{temp} graus Celsius em Fahrenheit é igual a {celsius_to_fahrenheit(temp)}')