# 18. (Soma de Diagonais de uma Matriz Quadrada) Receba uma matriz quadrada de inteiros e calcule a soma dos elementos das diagonais principal e secundária.

matrix = [
  [1, 2, 3],
  [4, -5, 6],
  [7, 8, 9]
]

def sumMatrix(matrix):
  i = 0
  mainDiagonal = 0
  secondDiagonal = 0
  for row in matrix:
    mainDiagonal += row[i]
    secondDiagonal += row[-1 if i == 0 else -i - 1]
    i += 1
  return mainDiagonal + secondDiagonal

print(sumMatrix(matrix))