#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

student1 = str(input('Enter with a first student: '))
student2 = str(input('Enter with a second student: '))
student3 = str(input('Enter with a third student: '))
student4 = str(input('Enter with a fouth student: '))
student_list = [student1, student2, student3, student4]
student_selection = choice(student_list)

print(f'The selected student is: {student_selection}')