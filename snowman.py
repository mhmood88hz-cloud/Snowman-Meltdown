import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word with underscores."""
    # Zeige die aktuelle ASCII-Art basierend auf den Fehlern
    print(STAGES[mistakes])

    # Erstelle die Anzeige für das Wort (z.B. _ _ _ _ _)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: " + display_word.strip())
    print(f"Mistakes: {mistakes} / {len(STAGES) - 1}\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Spielschleife läuft, solange der Schneemann nicht komplett geschmolzen ist
    while mistakes < len(STAGES) - 1:
        # Zustand anzeigen
        display_game_state(mistakes, secret_word, guessed_letters)

        # Eingabe fordern
        guess = input("Guess a letter: ").lower()

        # Zum Testen erhöhen wir die Fehler bei jedem Durchlauf,
        # damit man sieht, wie der Schneemann schmilzt!
        mistakes += 1

    # Zeige den final geschmolzenen Zustand am Ende
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game Over! The snowman melted.")


if __name__ == "__main__":
    play_game()
