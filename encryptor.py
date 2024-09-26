# Encrypting the base "Hello World" with an encrypt key
# The key is decided by the user input
# The encryptor will decode the letters into their numbers in the alphabet and then add both on top of each other
# If the number surpasses 26 (the maximum number of letters in the alphabet), it'll restart from the first letter A
# If the letter is the space " " then we will leave it as a " "
# Enjoy reading with this file!

base = "Hello world"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def Decode(text):
    index = 0
    decoded_list = []
    
    while index < len(text):
        char = text[index].lower()
        
        if char in alphabet:
            numberized = alphabet.find(char)
        else:
            numberized = -1
        
        decoded_list.append(numberized)
        index += 1
    return decoded_list

def Encrypt():
    key = str(input("What's the input key: "))
    keyDecoded = Decode(key)
    baseDecoded = Decode(base)

    index = 0
    finalList = []
    
    while index < len(baseDecoded):
        final = ""
        if baseDecoded[index] == -1:
            final = " "
        else:
            shift = (baseDecoded[index] + keyDecoded[index % len(keyDecoded)]) % len(alphabet)
            final = alphabet[shift]
        finalList.append(final)
        index += 1

    finalText = "".join(finalList)
    print(finalText)

Encrypt()
