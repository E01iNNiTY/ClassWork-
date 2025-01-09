import random

def roll_dice():
    rolled_numbers = []  

    while True:
        user_input = input("Press Enter to roll or type 'q' to quit: ").strip().lower()
        if user_input == 'quit':
            print("You exited the program. The numbers you rolled are:", rolled_numbers)
            break
        elif user_input == '':
            roll = random.randint(1, 6)
            rolled_numbers.append(roll)  
            print(f"You rolled a {roll}!")
        else:
            print("This is not valid input.")

if __name__ == "__main__":
    roll_dice()
