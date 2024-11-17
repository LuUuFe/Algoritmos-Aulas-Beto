# 13. (Média com Notas Maiores que a Média) Peça uma lista de notas de alunos e calcule a média. Em seguida, retorne uma lista com as notas que são maiores do que a média.

from functools import reduce

estudentsGrade = [7.5, 8, 4, 2, 6, 9, 7, 5, 10, 8, 6, 7]

def average(grades):
  avg = reduce(lambda x, y: x + y, grades) / len(grades)
  return avg

print(list(filter(lambda x: x > average(estudentsGrade), estudentsGrade)))