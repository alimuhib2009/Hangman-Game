import random
from words import words
import string
from hangman_visual import lives_visual_dict



def getValidWord (words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return  word.upper()    


def hangman():
    word = getValidWord(words)    
    word_letters = set(word)   #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   #  what the user has guessed

    lives = 6
    #getting user input
    while len(word_letters) > 0 and lives > 0:

        print('You have ' , lives ,'lives left and You have used these letters: ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print(lives_visual_dict[lives])

        print('current word: ', ' '.join(word_list))



        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("letters is not in word")
        elif user_letter in used_letters:
            print('You have already used that character. please try again.')

        else:
            print('Invalid character. Please try again')

    if lives == 0:
        print('you died, sorry. The word was', word)
    else:
        print('you guessed the word', word , '!!')    


hangman()  
