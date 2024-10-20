import random

WORDLIST = ['input', 'ocean', 'bring', 'under', 'night', 'xylos', 'dream', 'house', 'think', 'voice',  'happy', 'about', 'river', 'magic', 'offer', 'blame', 'dance', 'xenon', 'youth', 'water',  'sound', 'zebra', 'watch', 'laugh', 'great', 'apple', 'march', 'found', 'value', 'jolly',  'jumps', 'could', 'knife', 'right', 'queen', 'north', 'enjoy', 'pride', 'plant', 'grape',  'tiger', 'zippy', 'image', 'urban', 'quiet', 'lemon', 'skill', 'flash', 'young', 'knows']
RED = "🔴"
YELLOW = "🟡"
GREEN = "🟢"

def generateWord():
    index = random.randint(1, len(WORDLIST))
    return WORDLIST[index - 1]

def getInput(used, word):
    INPUT = False
    
    while INPUT == False:
        userInput = input("What's your guess: ")
        
        if userInput == "STOPTHEGAME":
            continueGame()
            return True
        elif userInput.lower() in used:
            print("This word has already been guessed!")
            continue
        elif (userInput.lower()).isalpha() == False:
            print("Only input letters, not numbers!")
            continue
        elif len(userInput) != len(word):
            print(f"You need a {len(word)}-letter word!")
            continue
        else:
            INPUT = True
            return userInput

def sortIntoList(word):
    returnList = []
    
    index = 0
    
    for letter in word:
        returnList.append(word[index])
        index += 1
    
    return returnList

def screenOutput(userInput, word):
    color1 = ""
    color2 = ""
    wordOutput = ""
    wordList = []
    
    wordList = sortIntoList(word)
    
    index = 0
    
    for letter in word:
        if userInput[index] == word[index]:
            color1 += GREEN
            listIndex = wordList.index(userInput[index])
            wordList.remove(wordList[listIndex])
        else:
            color1 += RED

        index += 1
    
    index = 0
    
    for letter in color1:
        if color1[index] == GREEN:
            color2 += GREEN
        elif color1[index] == RED:
            if userInput[index] in wordList:
                color2 += YELLOW
            else:
                color2 += RED
        
        index += 1
    
    index = 0
    
    for letter in userInput:
        wordOutput += userInput[index]
        if index < len(userInput) - 1:
            wordOutput += "|"
        index += 1
    
    print(f"\n{color2}")
    print(wordOutput)
    
    if not RED in color2 and not YELLOW in color2:
        return True
    else:
        return False

def continueGame():
    INPUT = False
    
    while INPUT != True:
        userInput = input(f"\nContinue the game? (y for yes and n for no): ")
        
        if userInput == "y":
            main()
            INPUT = True
        elif userInput == "n":
            print(f"\nThank you for playing the game!")
            INPUT = True
        else:
            print(f"\nInvalid command!")
            INPUT = False
            continue

def main():
    word = generateWord()
    tries = len(word) + 2
    
    print("Welcome to the Wordle Game!")
    print(f"Your challenge for today is a {len(word)}-letter word.")
    print(f"You have {tries} tries")
    
    
    WIN = False
    used = []
    
    turn = 0
    
    while turn < tries:
        userInput = getInput(used, word)
        
        if userInput == True:
            turn = tries
            continue
        
        used.append(userInput)
        
        WIN = screenOutput(userInput, word)
        
        turn += 1
        
        if WIN == True:
            print(f"\nCongrats! You have guess the word '{word}' in {turn} tries.")
            break
        else:
            print(f"\nYou got {tries - turn} tries left.")
            continue
    
    if WIN == False:
        print(f"Womp womp! The word is {word}.")
    
    if not userInput is True:
        continueGame()

if __name__ == "__main__":
    main()
