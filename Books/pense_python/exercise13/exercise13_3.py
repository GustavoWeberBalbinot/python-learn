'''
Altere o programa do exercício anterior para exibir as 20 palavras mais frequentes do livro.
'''
from exercise13_2 import format_txt, read_archive

my_archive = 'Books/pense_python/exercise13/file13-2.txt'
txt = read_archive(my_archive)
all_values_dict = format_txt(txt) #I left the function "activated" in the other file, and that's why the amount different word appears twice.

#I understand that not is best deployment, because the program analyzes the Dicitonary after he are creat, best deployment would be in the  function FORMAT_TXT, because the creat the list with analyzes the dicitonary in the same time is the best deployment I think

def the_twenty_amount_words(d: dict = dict()): #This "improvisation" is to the python interpret understand D as a dicitonary
    list_amount_words = list()
    for key, value in d.items():
        if len(list_amount_words) == 20:
            for x in range(0, 20): #I dont like FOR to improve this deployment but i cant think of any other idea. FOR to this deployment that not so bad, because all numbers is very low, and break in the first for .I tried binary search and I dont like this way.
                if x == 0 and value < list_amount_words[x][0]:
                    break
                if value >= list_amount_words[x][0] and x == 19:
                    list_amount_words.insert(x,[value, key])
                    list_amount_words.pop(0)
                    list_amount_words = sorted(list_amount_words)
                    break
                if value > list_amount_words[x][0]:
                    continue
                if value < list_amount_words[x][0]:
                    list_amount_words.insert(x, [value, key])
                    list_amount_words.pop(0)
                    list_amount_words = sorted(list_amount_words)
                    break

        else:
            list_amount_words.append([value,key])
            list_amount_words = sorted(list_amount_words)
    return list_amount_words



print(the_twenty_amount_words(all_values_dict))
