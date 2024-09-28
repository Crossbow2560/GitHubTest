from HangmanData import words, hangmanPics
import random


def getWord():
    global word, length
    num = random.randint(0, len(words) + 1)
    word = words[num]
    length = len(word)


def getLetters():
    wordSplit = [*word]
    return wordSplit


def getInput():
    letter = str.lower(input("Enter letter: "))
    return letter


def game():
    global tries
    yn = input("Welcome to hangman\n Start game?(y/n): ")
    if str.lower(yn) == 'y':
        pass
    elif str.lower(yn) == 'n':
        exit(0)
    else:
        print("Invalid Option")
        exit(0)
    getWord()
    tries = 0
    string = '_' * length
    wordsGiven = []
    while tries < 6:
        print(hangmanPics[tries])
        print(string)
        letters = getLetters()
        letter = getInput()
        if letter in wordsGiven:
            pass
        else:
            wordsGiven.append(letter)
        letterCount = letters.count(letter)
        if letterCount == 0:
            tries += 1
        else:
            pos = []
            for posi in range(0, length):
                if letter == letters[posi]:
                    pos.append(posi)
                else:
                    pass
            for cursor in range(0, length):
                if cursor in pos:
                    stringList = list(string)
                    stringList[cursor] = letter
                    string = "".join(stringList)
                else:
                    pass
        print(f"Words Used: {wordsGiven}")
        if string == word:
            break
    if tries == 6:
        print(hangmanPics[6]) 
        print(f"The Word Was: {word}")
        print("Game Over!\nYou Lose!")
        game()
    else:
        print(f"The Word Is: {word}")
        print("You Win")
        game()


game()
