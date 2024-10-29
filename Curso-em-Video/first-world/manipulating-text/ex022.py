#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

name = str(input('Enter with your name: '))
name_split = name.split()
name_all = name.replace(' ', '')

print(f'Your name with capital letters: {name.upper()}')
print(f'Your name with lowercase letters: {name.lower()}')
print(f'Your name have {len(name_all)} numbers')
print(f'Your first name have {len(name_split[0])} numbers ')
