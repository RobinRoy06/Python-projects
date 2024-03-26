#Get input from user
#Create a dice based apon input
#E.g input 2, 2 sided dices, 6, 6 sided, etc. etc.
#Cannot be odd number
#How to represent dice? - text




import random 

def roll():  
    result = random.randint (1, dice_input)
    print(f"You rolled a {result}")

try:

    dice_input = int(input("Enter which even-sided dice you'd like: d"))
    if dice_input <= 0 and dice_input % 2 != 0:
        print("Your input must be a positive even integer.")
    else:
        while True:
            roll_again = input("Would you like to roll again? (y/n): ").lower()
            if roll_again == "y":
                roll()
            else:
                print("Thank you for playing!")
                break

except ValueError:
   print("You must input an integer.")


    
