import random

print("Welcome to a game of numbers where you try to guess a randomly generated number, with easy, medium and hard modes available.")

difficulties = {
            "easy" : {"range" : 50, "attempts" : 10},
            "medium" : {"range" : 100, "attempts" : 7},
            "hard" : {"range" : 500, "attempts" : 5}
        }

def restart():
    yes_no = input("Would you like to play again? ")
    return yes_no.lower() == 'yes'

def play_game():
    game_running = True
    while game_running:
        try:
            difficulty = input("Please choose easy (1-50), medium (1-100) or hard (1-500) mode: ").lower()
            num = random.randint(1, difficulties[difficulty]["range"])
            count = difficulties[difficulty]["attempts"]

        except ValueError:
            print("Please input a valid integer value.")
            continue

        except KeyError:
            print("Invalid difficulty mode, please try again.")
            continue
    
        while True:
            if count == 0:
                print(f"Out of guesses! The number was {num}.")
                if restart():
                    break
                else:
                    game_running = False
                    break
                    
            try:
                user_num = int((input(f"You have {count} attempts remaining. Enter a number between 1 and {difficulties[difficulty]['range']}: ")))
            except ValueError:
                print("Please enter an integer value.")
                continue
    
            if not 1 <= user_num <= difficulties[difficulty]["range"]:
                print("Out of range, please try again.")
                continue
            elif user_num > num:
                count -= 1
                print(f"Too high! Try again. {difficulties[difficulty]['attempts'] - count} attempt(s) used.")
                continue
            elif user_num < num:
                count -= 1
                print(f"Too low! Try again. {difficulties[difficulty]['attempts'] - count} attempt(s) used." )
                continue
            else:
                count -= 1
                print(f"You got it! {difficulties[difficulty]['attempts'] - count} attempt(s) used.")
                if restart():
                    break
                else:
                    game_running = False
                    break

play_game()