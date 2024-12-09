# words.txt, de http://thinkpython2.com/code/words.txt.
#This website doesn't work 
#Skip this exercise

'''''
#New commands
#open('words.txt') --> # "open" the file

#fin.readline() === 'aa\r\n' --> # An object, with the function of search files. This object have many of reading, including readline. Read all characters until you reach a new line command

#The sequence \r\n represents \r-->'car return', return to line start. \n--> 'Line feed' advance to new line. \r\n--> Return to start line and new line.
#\r\n == Whitespace.

#strip --> remove Whitespace --> \r\n

#Comand to read line to line

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
    
'''