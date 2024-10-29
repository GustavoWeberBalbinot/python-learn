#Leia nome, ano de nascimento, carteira de trabalho(se for 0 para) (senão=), ano de contratação, salário
#Cadastrar em um dicionário
#Mostre tudo e também =   quantos anos a pessoa vai se aposentar

from datetime import date

year_today = date.today().year
info_people_dict = {'name': str(input('Enter your name: ')),
                    'age': year_today - int(input('Enter your birth year: ')),
                    'work card': int(input('Enter your work card: [0 if not available] '))
                    }

if info_people_dict['work card'] != 0:
    info_people_dict['year of hire'] = int(input('Enter your year of hire: '))
    info_people_dict['salary'] = int(input('Enter your salary: '))
    info_people_dict['retirement'] = info_people_dict['age'] + ((info_people_dict['year of hire'] + 35) - year_today)

print('-=-'*30)
for k, v in info_people_dict.items():
    print(f'Your {k} has the value: {v}')
print('-=-'*30)