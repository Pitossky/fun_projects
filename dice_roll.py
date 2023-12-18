import random
import os

def num_die():
    while True:
        try:
            num_dice = input("Number of dice: ")
            valid_inputs = ["1", "one", "2", "two"]
            if num_dice not in valid_inputs:
                raise ValueError("1 or 2 only")
            else:
                return num_dice
        except ValueError as err:
            print(err)

def dice_roll():
    min_val = 1
    max_val = 6
    roll_again = "yes"

    while roll_again.lower() == "yes":
        print("os name is: ", os.name)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"os module: {os.system('cls' if os.name == 'nt' else 'clear')}")
        amount = num_die()

        if amount == "2" or amount == "two":
            print("Rolling the dice...")
            dice_1 = random.randint(min_val, max_val) 
            dice_2 = random.randint(min_val, max_val)

            print("The values are:")
            print("Dice 1: ", dice_1)
            print("Dice 2: ", dice_2)
            print("Total: ", dice_1 + dice_2)

            roll_again = input("Roll again? ")

        else:
            print("Rolling the dice...")
            dice_1 = random.randint(min_val, max_val) 
            print(f"The value is: {dice_1}")

            roll_again = input("Roll again? ")

if __name__ == '__main__':
    dice_roll()
            


