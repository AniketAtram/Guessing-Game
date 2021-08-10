import random
from guessing_game_art import title

print(title)
print("""
WELCOME TO GUESS THE NUMBER.
RULES:
1.SELECT APPROPRIATE DIFFICULTY TO BEGIN WITH.
2.IF YOU CHOSE HARD DIFFICULTY YOU WILL GET 5 LIVES, OTHERWISE IF YOU GO WITH EASY DIFFICULTY YOU GET 10 LIVES.
3.GUESS A NUMBER BETWEEN 1-100.
4.IF THE NUMBER YOU'VE GUESSED IS HIGHER THAN THE ACTUAL NUMBER, YOU WILL BE PROMPTED TO GUESS LOWER,OTHERWISE 
YOU'LL BE PROMPTED TO GO HIGHER. HAVE FUN!!\n""")


def SELECT_DIFFICULTY():
    difficulty = input("ENTER 'E' FOR EASY AND 'H' FOR HARD: ").upper()
    if difficulty == "E":
        return 10
    elif difficulty == "H":
        return 5


WINNING_NUMBER = random.randint(1, 100)
LIVES = SELECT_DIFFICULTY()
GAME_OVER = False

while not GAME_OVER:
    print(f"Number of lives remaining {LIVES}")
    input_number = int(input("Enter number: "))
    if input_number > WINNING_NUMBER:
        print("LOWER!")
        LIVES -= 1
    elif input_number < WINNING_NUMBER:
        print("HIGHER!")
        LIVES -= 1
    elif input_number == WINNING_NUMBER:
        print(f"The number was {WINNING_NUMBER}")
        print("You Won!")
        GAME_OVER = True
    if LIVES == 0:
        print("You ran out of lives! GAME OVER!")
        print(f"The number was {WINNING_NUMBER}")
        GAME_OVER = True