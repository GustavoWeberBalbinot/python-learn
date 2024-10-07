#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida

score_note1 = float(input('Enter with a first note: '))
score_note2 = float(input('Enter with a second note: '))

media = (score_note1 + score_note2) / 2

if media < 5:
    print('You are failed')
elif media > 5 and media < 6.9:
    print('You need to do the recovery')
elif media >= 7:
    print('You passed')