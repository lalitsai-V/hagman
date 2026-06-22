import random

words = ["python", "computer", "programming", "hangman", "developer"]

wins = 0
losses = 0

while True:

    word = random.choice(words)
    guessed_letters = []
    lives = 6

    print("\n" + "=" * 40)
    print("       HANGMAN GAME")
    print("=" * 40)

    while lives > 0:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Lives Remaining:", lives)
        print("Guessed Letters:", guessed_letters)

        if "_" not in display_word:
            print("\n Congratulations! You guessed the word:", word)
            wins += 1
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print("Wrong Guess!")

    else:
        print("\n Game Over!")
        print("The word was:", word)
        losses += 1

    print("\nStatistics")
    print("Wins :", wins)
    print("Losses :", losses)

    choice = input("\nPlay Again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThanks for Playing!")
        break
