import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#======כאן יש להוסיף אוסף של מילים=====
words = ['Class', 'Shira', 'Green', 'Red', 'Encyclopedia', 'Black', 'Data structures']
#============כאן יכתבו הפונקציות=============
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print("The missed letters "+missedLetters+" !")
    for i in secretWord:
        if i in correctLetters:
            print(""+i, end="")
        else:
            print("_", end="")

    print("\n")

def getGuess(alreadyGuessed):
    guesseN = input("Please enter letter!")
    if guesseN in alreadyGuessed:
        print("You already guessed!")
    elif guesseN.isalpha():
        print("This is letter!!")
        return guesseN
    else:
        return 'x'

def playAgain():
    choose = input("Do you want to play again?(Y/N)\n")
    if choose == 'Y' or choose == 'y':
        return True
    else:
        return False

#========כאן תחילת המשחק================
missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = words[random.randrange(len(words))]
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # המשתמש מקיש אות ובודקים אם זה תקין
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # בדיקה אם השחקן ניצח
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # בדיקה האם השחקן הפסיד
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # האם השחקן רוצה לשחק שוב?? 
	#אתחול המשתנים והמשחק מתחדש...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = words[random.randrange(len(words))]
        else:
            break