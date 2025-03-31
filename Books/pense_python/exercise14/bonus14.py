import os

for root, dirs, files in os.walk('Books'):
    print(root, end='')
    print(str(dirs).replace("'",'').replace('[','').replace(']',''), end='/\n')
    for x in range(len(files)):
        print(files[x], end='\n')
    print()