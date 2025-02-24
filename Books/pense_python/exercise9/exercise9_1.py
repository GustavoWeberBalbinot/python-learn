with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

def the_large_words(t = str()):
    t = t.split()
    for values in t:
        if len(values) >= 20:
            print(f'This word:{values}, have a more twenty letters = {len(values)}')

the_large_words(txt)