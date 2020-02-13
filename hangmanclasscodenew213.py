from __future__ import print_function
word = "earring"
letter = ""
updatedSpaces = ' _ '
lives = 6

def initialize():
    global word
    global updatedSpaces
    global letter
    word = 'earring'
    print((updatedSpaces*(len(word))))

def getLetter():
    global letter
    global lives
    global word
    print('Guess a letter.')
    letter = raw_input()
    if letter not in word: 
        print ('Lives:',lives-1)
    if letter in word:
        print ('Lives:6')

def win():
    global word
    if word == word:
        print('Yay, you won!!') 
    if word != word:
        print(getLetter)      
        
          
                         
def main():
    getLetter()
    initialize()
    
                    

main()     