import random
import math
#Hangman

word = ("watermelon", "banana", "apple", "orange")

hang_art = ('''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
)


random_word = random.choice(word)
guess_word = []
random_char = random.choice(random_word)
print(random_word)

for char in random_word:

    if not char == random.choice(random_char):
        guess_word.append("_ ")
    else:
        guess_word.append(char)

print(guess_word)

char_guess = input("Guess a Letter : ").upper()

for art in hang_art:
    if char_guess not in random_word:
        print(art)
    
