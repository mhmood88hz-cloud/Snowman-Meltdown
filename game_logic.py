import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Oops! '{guess}' is not in the word.")
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            break

    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! You saved the snowman! The word was: {secret_word}")
    else:
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"Game Over! The snowman melted completely. The word was: {secret_word}")
