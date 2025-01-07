students = []
teachers = []
disciplines = []
classes = []

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

def show_menu():
  while True:
    print("\nSistema Escolar")
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Professor")
    print("3. Cadastrar Disciplina")
    print("4. Cadastrar Turma")
    print("5. Sair")
    
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
      print("Saindo do sistema. Até logo!")
      break
    else:
      print("Opção inválida. Tente novamente.\n")

show_menu()