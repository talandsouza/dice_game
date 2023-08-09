import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    play_again = True

    while play_again:
        input("Press Enter to roll the dice...")
        dice1 = roll_dice()
        dice2 = roll_dice()

        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")

        total_score = dice1 + dice2
        print(f"Total Score: {total_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"

    print("Thank you for playing!")

if __name__ == "__main__":
    main()

