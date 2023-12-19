import random


HANGMAN = [
    '   _____ \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '__|__\n',
    '   _____ \n'
    '  |     | \n'
    '  |     | \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '__|__\n',
    '   _____ \n'
    '  |     | \n'
    '  |     | \n'
    '  |     | \n'
    '  |      \n'
    '  |      \n'
    '  |      \n'
    '__|__\n',
    '   _____ \n'
    '  |     | \n'
    '  |     | \n'
    '  |     | \n'
    '  |     O \n'
    '  |      \n'
    '  |      \n'
    '__|__\n',
    '   _____ \n'
    '  |     | \n'
    '  |     | \n'
    '  |     | \n'
    '  |     O \n'
    '  |    /| \n'
    '  |      \n'
    '__|__\n',
    '   _____ \n'
    '  |     | \n'
    '  |     | \n'
    '  |     | \n'
    '  |     O \n'
    '  |    /| \n'
    '  |    /| \n'
    '__|__\n',

]

WORDS = ['january', 'border', 'image', 'film', 'promise', 'kids',
       'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world']
    
MAX_WRONG_GUESSES = len(HANGMAN) - 1

word = random.choice(WORDS)

current_guess = '_' * len(word)

wrong_guesses = 0

guessed_letters = []

print("Welcome to Hangman")
print("Try to guess the word")

while wrong_guesses < MAX_WRONG_GUESSES and current_guess != word:
    print(HANGMAN[wrong_guesses])
    print("You have used the following letters: ", guessed_letters)
    print("So far the word is: ", current_guess)

    guess = input("Enter your guess: ").strip()
    while len(guess) == 0 or len(guess) > 1:
            print("Enter a single letter \n")
            guess = input('Enter one letter as guess: ').strip()
    
    while guess in guessed_letters:
        print(f"You have already guessed the letter {guess}")
        guess = input("Enter another guess: ").strip()

    guessed_letters.append(guess)

    if guess in word:
        print("Congratulations, You have guessed correctly!!")
        new_current_guess = ""

        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]
        
        current_guess = new_current_guess
    
    else:
        print("Sorry that was incorrect")
        wrong_guesses += 1

if wrong_guesses == MAX_WRONG_GUESSES:
    print(HANGMAN[wrong_guesses])
    print("You have been hanged!!")
    print("The correct word is: ", word)

else:
    print("You have won!!")

