import random
from hangman_words import word_list   # make sure hangman_words.py has a list called word_list

# ----- Banners -----
welcome = r''' 
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█
'''
print(welcome)

logo = r''' 
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
'''
print(logo)

# ----- Game setup -----
lives = 6

# Hangman stages (from 6 lives to 0 lives)
stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
      |
      |
      |
      |
========='''
]

# Choose a random word
secret_word = random.choice(word_list)
# print(secret_word)  # Uncomment for debugging

# Create initial display: all underscores
display = "_" * len(secret_word)
print(display)

game_over = False
correct_letters = []   # letters guessed correctly so far
wrong_letters = []     # wrong guesses

while not game_over:
    guess_letter = input("Guess a letter: ").lower()

    # Simple input validation
    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if letter was already guessed before
    if guess_letter in correct_letters or guess_letter in wrong_letters:
        print(f"You already guessed '{guess_letter}'. Try a different letter.")
        print(display)
        print(stages[lives])
        continue

    # Build new display string based on this guess
    new_display = ""

    for letter in secret_word:
        if letter == guess_letter:
            new_display += letter
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    # If the guessed letter is in the word
    if guess_letter in secret_word:
        correct_letters.append(guess_letter)
        display = new_display
        print(display)
    else:
        wrong_letters.append(guess_letter)
        lives -= 1
        print(f"'{guess_letter}' is not in the word. Lives left: {lives}")
        print(display)

        if lives == 0:
            game_over = True
            print("---------- You lose! ----------")
            print(f"The word was: {secret_word}")

    # Check win condition
    if "_" not in display:
        game_over = True
        print("----------- You win! -----------")

    # Show current hangman stage
    print(stages[lives])
