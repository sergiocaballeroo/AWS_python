def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
def getMessage():
    
    stringToEncrypt = input("Please enter a message to encrypt: ")
    if stringToEncrypt == ("") or len(stringToEncrypt) < 3:
        print("Invalid, please enter a valid message")
    else:
        return stringToEncrypt
        
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    if len(shiftAmount) > 25 or len(shiftAmount) < 0:
        print("Invalid, please enter a valid key")
    else:
        return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentChar in uppercaseMessage:
        position = alphabet.find(currentChar)
        newPosition = position + int (cipherKey)
        if(currentChar in alphabet):
            encryptMessage = encryptMessage + alphabet[newPosition]
        else:
            encryptMessage = encryptMessage + currentChar
    
    return encryptMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {alphabet}')
    alphabet_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {alphabet_2}')
    
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, alphabet_2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, alphabet_2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()