#As seguintes funções pretendem verificar se uma string contém alguma letra minúscula, mas algumas delas estão erradas. Para cada função, descreva o que ela faz (assumindo que o parâmetro seja uma string).


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        #Incorrect program, this program verify only the first letter

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        #Incorrect program, this program does not verify the letter in the word, this program verify the letter 'c', and the return is a string ('True' or 'False') this will probaly cause a problem

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
    #Incorrect program, this program have a problem, because if the last letter does not is lowercase the program fails


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    #Correct program, if the letter in word is lowercase, return True, and the flag = True (flag = true or false --> [flag=True]) or return True if a value is True

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
    #Incorrect program, if the word have letter lowercase in the last letters, and uppercase in the start word this prorgram return False and finish (verify all letters is lowercase does not one letter)