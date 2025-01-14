'''
Escreva uma função chamada in_bisect que receba uma lista ordenada, um valor-alvo e devolva o índice do valor na lista se ele estiver lá, ou None se não estiver.

Ou você pode ler a documentação do módulo bisect e usá-lo!
'''
sorted_lists =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_list = [4, 7, 9, 12, 15, 18, 21, 23, 25, 27, 30, 32, 35, 37, 39, 41, 43, 45, 47, 49, 
               51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 
               91, 93, 95, 97, 99, 101, 103, 105, 107, 109]

target_value = 21


def in_bisect(list_target, target_value):
    high_value = len(list_target) - 1
    lower_value = 0
    actual_position = high_value // 2
    count = 0
    while lower_value <= high_value:
        count += 1
        actual_position = (lower_value + high_value) // 2
        if target_value == list_target[actual_position]:
            return count
        elif target_value > list_target[actual_position]:
            lower_value = actual_position + 1
        else:
            high_value = actual_position - 1
        
    return None


print(in_bisect(sorted_list, target_value))
