# 6. (Cálculo de Média Aritmética) Peça três notas de um aluno e calcule a média aritmética delas.

grade1 = int(input('Digite a primeira nota: '))
grade2 = int(input('Digite a segunda nota: '))
grade3 = int(input('Digite a terceira nota: '))

def average(grade1, grade2, grade3):
  average = round((grade1 + grade2 + grade3) / 3, 2)
  return average

print(f'A média das notas é igual a {average(grade1, grade2, grade3)}')