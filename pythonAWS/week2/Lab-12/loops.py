import random 

def gameGuess():

    print("\tGuess the number")
    print("The rules are simple, i'll think of a number and you'll try to guess it")
    
    number = random.randint(1,10)
    isGuessRight = False
    
    while isGuessRight != True:
        guess = input("Guess a number between 1 and 10: \n")
        
        if int(guess) == number:
            print("You guessed {}. YOU WIN ".format(guess))
            isGuessRight = True
        else:
            print("Keep trying, number is: {}".format(guess))


def Exercise1():
    number = int(input("Give me a number between 1 and 8"))
    
    for i in range (number):
        print("*"*(i+1))
        
        
def Exercise2():
    number = 1
    for i in range(1, 10):
        print(i*number)
        number+=1;
        if int(number)==10:
            number = 1
Exercise2()