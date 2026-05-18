import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown", "code", "pycharm"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word with underscores."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: " + display_word.strip())
    print(f"Mistakes: {mistakes} / {len(STAGES) - 1}\n")


def run_single_match():
    """Runs a single round of the snowman game. Returns True if won, False if lost."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nA new secret word has been selected!")
    # Zum Testen kannst du die nächste Zeile einkommentieren:
    # print(f"[DEBUG] Secret word: {secret_word}")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        # Eingabevalidierung
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid alphabetical character.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            break

    # Spielende auswerten
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\n🎉 Congratulations! You saved the snowman! The word was: {secret_word}\n")
    else:
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"\n💀 Game Over! The snowman melted completely. The word was: {secret_word}\n")


def play_game():
    """Main game entry point handling the replay option loop."""
    print("Welcome to Snowman Meltdown!")

    while True:
        run_single_match()

        # Wiederspiel-Option abfragen
        replay = input("Do you want to play again? (y/n): ").lower().strip()
        while replay not in ['y', 'n']:
            replay = input("Please enter 'y' for yes or 'n' for no: ").lower().strip()

        if replay == 'n':
            print("Thanks for playing Snowman Meltdown! Goodbye!")
            break
