#crie maior(), recebe vários parâmetros inteiros.

def maior(* num):
    major = 0
    for x in range(0,len(num)):
        if num[x] > major:
            major = num[x]
    return major

print(maior(1,5,9,3,4,6))