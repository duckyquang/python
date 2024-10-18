import random

wordList = ['apple', 'cat', 'orange', 'chair', 'enzyme', 'laptop', 'math']
red = "🔴"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def generateWord():
    index = random.randint(1, len(wordList))
    return wordList[index - 1]

def findLetter(letter, word):
    return word.find(letter)

def getInput(used):
    i = False
    
    while i == False:
        answer = input("Select a letter: ")
        
        if answer in used:
            print("Letter already used!")
            continue
        elif alphabet.find(answer.lower()) == -1:
            print("Only input letters!")
            continue
        elif len(answer) != 1:
            print("Input 1 letters!")
            continue
        else:
            return answer
            i = True

def output(used, word):
    index = 0
    string = ""
    
    while index < len(word):
        if word[index] in used:
            string += word[index]
        else:
            string += red
    
    return string
            

def main():
    win = False
    
    word = generateWord()
    used = []
    
    while win != False:
        userInput = getInput(used)
        used.append(userInput)
        
        if findLetter(userInput, word) == -1:
            print("Wrong letter.")
        
        output = output(used, word)
        print(output)
        
        if red not in output:
            print("Congrats! You have finished the wordle.")
        else:
            continue

main()
