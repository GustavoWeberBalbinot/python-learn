# c = colors
c = ('\033[0;0;0m',  # No color 0
     '\033[0;0;40m',  # White 1
     '\033[0;0;41m',  # Red 2
     '\033[0;0;42m',  # Green 3
     '\033[0;0;43m',  # Yellow 4
     '\033[0;0;44m',  # Blue 5
     '\033[0;0;45m')  # Purple 6

def title(text, color=0):
    size = len(text) + 4
    print(c[color])
    print('-' * size)
    print(text)
    print('-' * size)

def helpme(text='end'):
    title(text, 6)
    print(c[3], end='')
    help(text)

# main program
while True:
    title('Command Help System', 4)
    print(c[5], end='')
    commands = str(input('Enter a command to see its HELP. [END to finish]: ').strip())
    if commands.upper() == 'END':
        print(c[2], end='')
        print('Finished')
        break
    else:
        helpme(commands)
