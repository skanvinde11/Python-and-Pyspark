import random

user_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors"))
pc_choice = random.randint(0,2)
print(f"Computer chose : {pc_choice}")

if user_choice == 0 and pc_choice == 2:
    print("You win")
elif pc_choice == 2 and user_choice == 0:
    print("You lose")
elif pc_choice > user_choice:
    print("Computer Wins")
elif user_choice > pc_choice:
    print("You win")
elif  user_choice >= 3 or user_choice <0:
    print("You typed an invalid number! You lose be default!")
elif  pc_choice == user_choice:
    print("It's a draw")
