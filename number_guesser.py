import random


HIGHER_RESPONSES = [
    "Okay, going higher! Let me think...",
    "Higher it is! Narrowing it down...",
    "Got it, aiming higher now...",
    "Interesting! Moving up the range...",
]

LOWER_RESPONSES = [
    "Alright, trying lower! Almost there...",
    "Lower? No problem, adjusting...",
    "Got it, coming down a bit...",
    "Understood, shifting lower...",
]

CORRECT_RESPONSES = [
    "I guessed your number! I knew I'd crack it!",
    "Yes! Got it! Binary search never fails!",
    "Nailed it! Your number is mine!",
    "Correct! I love a good guessing game!",
]


def get_random_response(responses):
    return random.choice(responses)


def get_difficulty():
    while True:
        difficulty = input("Choose difficulty ('easy' for 1-100 or 'hard' for 1-500): ").strip().lower()
        if difficulty == "easy":
            return 1, 100
        elif difficulty == "hard":
            return 1, 500
        else:
            print("Hmm, that's not a valid choice. Please type 'easy' or 'hard'.")


def get_feedback(guess):
    while True:
        feedback = input("Is my guess too low, too high, or just right? ('higher', 'lower', or 'correct'): ").strip().lower()
        if feedback in ("higher", "lower", "correct"):
            return feedback
        else:
            print("Please type 'higher', 'lower', or 'correct'. Nothing else will do!")


def play_game():
    print("\n" + "=" * 45)
    print("     Welcome to the Number Guesser Bot!")
    print("=" * 45)

    start = input("\nType 'guess' to start: ").strip().lower()
    if start != "guess":
        print("That's not 'guess'. Come back when you're ready!")
        return

    low, high = get_difficulty()

    print(f"\nAlright! Think of a number between {low} and {high}.")
    print("Keep it secret! I'll figure it out.\n")

    attempts = 0

    while True:
        guess = (low + high) // 2
        print(f"\nMy guess is: {guess}")

        feedback = get_feedback(guess)
        attempts += 1

        if feedback == "correct":
            print(f"\n{get_random_response(CORRECT_RESPONSES)}")
            print(f"It took me {attempts} {'guess' if attempts == 1 else 'guesses'} to find your number.")
            break

        elif feedback == "higher":
            print(get_random_response(HIGHER_RESPONSES))
            low = guess + 1

        elif feedback == "lower":
            print(get_random_response(LOWER_RESPONSES))
            high = guess - 1

        if low > high:
            print("\nSomething doesn't add up — the hints seem inconsistent.")
            print("Are you sure you picked a valid number and gave correct hints?")
            print("Let's start fresh!")
            break


def ask_replay():
    while True:
        again = input("\nWant to play again? ('yes' or 'no'): ").strip().lower()
        if again in ("yes", "y"):
            return True
        elif again in ("no", "n"):
            return False
        else:
            print("Just 'yes' or 'no' will do!")


def main():
    while True:
        play_game()
        if not ask_replay():
            print("\nThanks for playing! Come back anytime.")
            print("=" * 45 + "\n")
            break


if __name__ == "__main__":
    main()