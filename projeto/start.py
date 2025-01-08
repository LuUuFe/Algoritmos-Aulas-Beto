students = [
  {
    'name': 'João Silva',
    'registration': 'S001',
    'dateOfBirth': '10/05/2005',
    'gender': 'Masculino',
    'address': 'Rua A, 123',
    'phone': '1111-2222',
    'email': 'joao.silva@email.com'
  },
  {
    'name': 'Maria Oliveira',
    'registration': 'S002',
    'dateOfBirth': '15/08/2006',
    'gender': 'Feminino',
    'address': 'Rua B, 456',
    'phone': '3333-4444',
    'email': 'maria.oliveira@email.com'
  }
]

teachers = [
  {
    'name': 'Carlos Pereira',
    'registration': 'T001',
    'dateOfBirth': '20/03/1980',
    'gender': 'Masculino',
    'address': 'Avenida X, 789',
    'phone': '5555-6666',
    'email': 'carlos.pereira@email.com',
    'discipline': 'Matemática'
  },
  {
    'name': 'Ana Souza',
    'registration': 'T002',
    'dateOfBirth': '12/07/1985',
    'gender': 'Feminino',
    'address': 'Avenida Y, 101',
    'phone': '7777-8888',
    'email': 'ana.souza@email.com',
    'discipline': 'Português'
  }
]

disciplines = [
  {
    'name': 'Matemática',
    'code': 'D001',
    'workload': '80 horas',
    'teacher': 'Carlos Pereira'
  },
  {
    'name': 'Português',
    'code': 'D002',
    'workload': '60 horas',
    'teacher': 'Ana Souza'
  }
]

classes = [
  {
    'name': 'Turma A',
    'code': 'C001',
    'discipline': 'Matemática',
    'teacher': 'Carlos Pereira',
    'students': ['S001', 'S002']
  },
  {
    'name': 'Turma B',
    'code': 'C002',
    'discipline': 'Português',
    'teacher': 'Ana Souza',
    'students': ['S001']
  }
]

# Passando para informar que toda essa parte onde eu coleto os dados para cadastrar eu pedir para o ChatGPT terminar para mim!

def register_student():
  student = {
    'name': input('Digite o nome do aluno: '),
    'registration': input('Digite a matrícula do aluno: '),
    'dateOfBirth': input('Digite a data de nascimento do aluno (dd/mm/aaaa): '),
    'gender': input('Digite o sexo do aluno: '),
    'address': input('Digite o endereço do aluno: '),
    'phone': input('Digite o telefone do aluno: '),
    'email': input('Digite o e-mail do aluno: ')
  }
  students.append(student)
  print("Aluno cadastrado com sucesso!\n")

def register_teacher():
  teacher = {
    'name': input('Digite o nome do professor: '),
    'registration': input('Digite a matrícula do professor: '),
    'dateOfBirth': input('Digite a data de nascimento do professor (dd/mm/aaaa): '),
    'gender': input('Digite o sexo do professor: '),
    'address': input('Digite o endereço do professor: '),
    'phone': input('Digite o telefone do professor: '),
    'email': input('Digite o e-mail do professor: '),
    'discipline': input('Digite a disciplina do professor: ')
  }
  teachers.append(teacher)
  print("Professor cadastrado com sucesso!\n")

def register_discipline():
  discipline = {
    'name': input('Digite o nome da disciplina: '),
    'code': input('Digite o código da disciplina (ex: A1234): '),
    'workload': input('Digite a carga horária da disciplina: '),
    'teacher': input('Digite o nome do professor responsável: ')
  }
  disciplines.append(discipline)
  print("Disciplina cadastrada com sucesso!\n")

def register_class():
  classInfo = {
    'name': input('Digite o nome da turma: '),
    'code': input('Digite o código da turma (ex: A1234): '),
    'discipline': input('Digite o nome da disciplina da turma: '),
    'teacher': input('Digite o nome do professor da turma: '),
    'students': input('Digite as matrículas dos alunos separados por vírgula: ').split(',')
  }
  classes.append(classInfo)
  print("Turma cadastrada com sucesso!\n")

def filter_teachers_per_discipline():
  print([discipline['name'] for discipline in disciplines])
  disciplineSearch = input("Digite o nome da disciplina: ")
  teachersPerDiscipline = list(filter(lambda teacher: teacher['discipline'] == disciplineSearch, teachers))
  print([teacher['name'] for teacher in teachersPerDiscipline])

def enroll_student_in_class():
  studentRegistration = input("Digite a matrícula do aluno: ")
  classCode = input("Digite o código da turma: ")
  classFound = next((cls for cls in classes if cls['code'] == classCode), None)
  if classFound:
    classFound['students'].append(studentRegistration)
    print("Aluno matriculado com sucesso!\n")
  else:
    print("Turma não encontrada!\n")

def allocate_teacher_to_discipline():
  teacher_name = input("Digite o nome do professor: ")
  disciplineName = input("Digite o nome da disciplina: ")
  disciplineFound = next((discipline for discipline in disciplines if discipline['name'] == disciplineName), None)
  if disciplineFound:
    disciplineFound['teacher'] = teacher_name
    print("Professor alocado com sucesso!\n")
  else:
    print("Disciplina não encontrada!\n")

def allocate_discipline_to_class():
  disciplineName = input("Digite o nome da disciplina: ")
  classCode = input("Digite o código da turma: ")
  classFound = next((cls for cls in classes if cls['code'] == classCode), None)
  if classFound:
    classFound['discipline'] = disciplineName
    print("Disciplina alocada com sucesso!\n")
  else:
    print("Turma não encontrada!\n")

def consult_students_in_class():
  classCode = input("Digite o código da turma: ")
  classFound = next((cls for cls in classes if cls['code'] == classCode), None)
  if classFound:
    print("Alunos matriculados:", classFound['students'])
  else:
    print("Turma não encontrada!\n")

def consult_teachers_in_discipline():
  disciplineName = input("Digite o nome da disciplina: ")
  disciplineFound = next((discipline for discipline in disciplines if discipline['name'] == disciplineName), None)
  if disciplineFound:
    print("Professor alocado:", disciplineFound['teacher'])
  else:
    print("Disciplina não encontrada!\n")

def consult_disciplines_in_class():
  classCode = input("Digite o código da turma: ")
  classFound = next((cls for cls in classes if cls['code'] == classCode), None)
  if classFound:
    print("Disciplina alocada:", classFound['discipline'])
  else:
    print("Turma não encontrada!\n")

def show_menu():
  while True:
    print("\nSistema Escolar")
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Professor")
    print("3. Cadastrar Disciplina")
    print("4. Cadastrar Turma")
    print("5. Filtrar Professores Por Disciplina")
    print("6. Matricular Aluno em Turma")
    print("7. Alocar Professor em Disciplina")
    print("8. Alocar Disciplina em Turma")
    print("9. Consultar Alunos Matriculados em Turma")
    print("10. Consultar Professores Alocados em Disciplina")
    print("11. Consultar Disciplinas Alocadas em Turma")
    print("0. Sair")
    
    choice = input("Escolha uma opção: ")

    if choice == '1':
      register_student()
    elif choice == '2':
      register_teacher()
    elif choice == '3':
      register_discipline()
    elif choice == '4':
      register_class()
    elif choice == '5':
      filter_teachers_per_discipline()
    elif choice == '6':
      enroll_student_in_class()
    elif choice == '7':
      allocate_teacher_to_discipline()
    elif choice == '8':
      allocate_discipline_to_class()
    elif choice == '9':
      consult_students_in_class()
    elif choice == '10':
      consult_teachers_in_discipline()
    elif choice == '11':
      consult_disciplines_in_class()
    elif choice == '0':
      print("Saindo do sistema. Até logo!")
      break
    else:
      print("Opção inválida. Tente novamente.\n")
show_menu()