#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro aluns e mostre a ordem sorteada

from random import shuffle
student_list = list()

for x in range(0,4):
    student = str(input(f'Enther with a student {x}:'))
    student_list.append(student)

shuffle(student_list)

print(f'The sequence is:', end='')
for x in range(0,4):
    print(f' {student_list[x]}', end= '')