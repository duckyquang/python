# Encrypting the base "Hello World" with an encrypt key
# The key is decided by the user input
# The encryptor will decode the letters into their numbers in the alphabet then add it on top of each other
# If the number surpasses 26 (the maximum number of letters in the alphabat), it'll restart from the first letter A
# If the letter is the space " " then we will leave it as a " "
# Enjoy reading with this file!

base = "Hello world"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def Decode(text):
    index = 0
    list = []
    while index < len(text):
        numberized = alphabet.find(text[index].lower()) + 1
        list.append(numberized)
        index += 1
    return list
        

def Encrypt():
    key = str(input("What's the input key: "))
    keyDecoded = Decode(key)
    baseDecoded = Decode(base)
    
    index = 0
    finalList = []
    
    while index < len(baseDecoded):
        final = ""
        
        if int(baseDecoded[index]) == 0:
            final = " "
        else:
            final = alphabet[(int(baseDecoded[index]) + int(keyDecoded[index % 6]) - 1) % 27]
        
        finalList.append(final)
        index += 1
    
    finalText = ""
    finalText = finalText.join(finalList)
    print(finalText)
    

Encrypt()
