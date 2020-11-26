import random
import sys


words = [
    "grape",
    "blow",
    "toe",
    "mother",
    "wool",
    "toothbrush",
    "stocking",
    "insurance",
    "pleasure",
    "smile",
    "partner",
    "friend",
    "whistle",
    "calculator",
    "planes",
    "expert",
    "head",
    "houses",
    "glove",
    "punishment",
    "plastic",
    "achiever",
    "nose",
    "trucks",
    "knee",
    "powder",
    "detail",
    "kiss",
    "icicle",
    "waste",
    "science",
    "reaction",
    "dock",
    "party",
    "authority",
    "activity",
    "picture",
    "team",
    "string",
    "winter",
    "shoe",
    "grip",
    "rain",
    "appliance",
    "tax",
    "purpose",
    "copper",
    "hill",
    "ladybug",
    "snakes",
]

word = random.choice(words)
word = word.upper()
digits = str(len(word))
print('\nWelcome to Hangman. \n\nThe word we are looking for is ' + digits
      + ' characters long.')
print('You have 8 tries to guess the hidden word.')
word_display = '_' * len(word)
print(word_display)

for number in range(8):
    while True:
        letter = input('Please enter a letter or guess the word. ').upper()
        if letter.isalpha():
            break
        else:
            print('You cant enter a number.')

    if letter == word:
        print('Ow! ' + word + ' was a correct guess, you won!')
        break
    elif letter in word:
        times = word.count(letter)
        if times > 1:
            print('You guessed a letter, the letter ' + letter +
                  ' apeaers ' + str(times) + ' times in the word.')
            word_list = list(word_display)
            indices = [i for i, character in enumerate(
                word) if character == letter]
            for index in indices:
                word_list[index] = letter
            word_display = ''.join(word_list)
            if word_display == word:
                print("Nice! You have correctly guessed the word: " + word + " !")
                break

        else:
            print('You guessed a letter, the letter ' + letter +
                  ' apeaers 1 time in the word.')
            word_list = list(word_display)
            indices = [i for i, character in enumerate(
                word) if character == letter]
            for index in indices:
                word_list[index] = letter
            word_display = ''.join(word_list)
            if word_display == word:
                print("Nice! You have correctly guessed the word: " + word + "!")
                break

    else:
        print('This letter is not in the word, please try again.')

    print(word_display)
    turn = 7 - number
    print('\nYou have ' + str(turn) + ' turns left')
    if turn == 0:
        print('Game over, you are out of turns. The word was: ' + word + '.')
        break
