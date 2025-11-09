from game import NumberGuessGame

def main():
    print("🎯 Welcome to the Number Guessing Game!")
    game = NumberGuessGame(1, 50)

    while True:
        try:
            user_input = input("Enter your guess (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Goodbye!")
                break

            guess = int(user_input)
            result = game.guess(guess)
            print(result)

            if "Correct" in result:
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
