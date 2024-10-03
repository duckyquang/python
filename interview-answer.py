import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def Decode(string):
    index = 0
    list = []
    
    for letters in string:
        number = alphabet.find(string[index].lower()) + 1
        if number == -1:
            list.append(0)
        else:
            list.append(number)
        index += 1
    
    return list

def Encode():
    user_input = input("What's the text you want to input: ")
    almostFinalList = Decode(user_input)
    
    index = 0
    number = random.randint(1, 20)
    finalList = []
    
    for numbers in almostFinalList:
        if almostFinalList[index] == 0:
            finalList.append(" ")
        else:
            letterIndex = (almostFinalList[index] + number) % 27 - 1
            finalList.append(alphabet[letterIndex])
            
        index += 1
    
    print(f"The key is: {number}")
    print(f"The final list is: {finalList}")
    
Encode()
