import random

num_digits = 3
max_digits= 10

def main():
    print("bagels, logic game!".format(num_digits))

while True:
    secretNum = getSecretNum()
    print("I have thpught a number")
    print("Ypu have {} guesses to get it".format(max_digits))

    while numGuesses <= max_digits:
        while len(guess) != num_digits or not guess.isdecimal():
            print("GUess #{}: ".format(numGuesses))
            guess = input("> ")

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            break

        if numGuesses > max_digits:
            print("YYou run out of guess")
            print("The answer was {}. " .format(secretNum))

    print("Do you want to play again? Yes or No")
    if not input("> ").lower().startswith("Y"):
        break
print("Thank you for playing!")

def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)

    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    
    if len(clues) == 0:
        return "Bagels"
    else:
        return " ".join(clues)
    
if __name__ == "__main__":
    main()