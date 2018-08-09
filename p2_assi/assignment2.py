'''implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for char in secret_word:
        if char in  letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str_1 = ''
    for char in secret_word:
        if char in letters_guessed:
            str_1 = str_1 + char
        else:
            str_1 = str_1 +'_'
    return str_1


DICTIONARY=string.ascii_lowercase
def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_1 = ''
    for char in DICTIONARY:
        if char not in letters_guessed:
            str_1 = str_1 + char
    return str_1
    

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    intro = str(len(secret_word))
    letters_guessed = []
    guess = str
    mistakes_made = 8
    word_guessed = False
    
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is "+ intro + ("letters long."))
    print ("------------")

    while mistakes_made > 0 and mistakes_made <= 8 and word_guessed is False:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            word_guessed = True
            break
        print ("You have " + str(mistakes_made) + "guesses left.")
        print ("Available letters: " + get_available_letters(letters_guessed))
        guess =input("Please guess a letter: ".lower())
        if guess in secret_word:
            if guess in letters_guessed:
                print ("Oops! You've already guessed that letter: "+ get_guessed_word(secret_word, letters_guessed))
                print ("------------")
            else:
                letters_guessed.append(guess)
                print ("Good guess: "+ get_guessed_word(secret_word, letters_guessed))
                print ("------------")
        else:
            if guess in letters_guessed:
                print ("Oops! You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                print ("------------")
            else:
                letters_guessed.append(guess)
                mistakes_made -= 1
                print ("Oops! That letter is not in my word: "+ get_guessed_word(secret_word, letters_guessed))
                print ("------------")

    if word_guessed == True:
        print("Congratulations, you won!") 
    elif mistakes_made == 0:
        print (("Sorry, you ran out of guesses. The word was ") + secret_word)
def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secret_word = choose_word(word_list).lower()
    hangman(secret_word)


if __name__== "__main__":
    main()
