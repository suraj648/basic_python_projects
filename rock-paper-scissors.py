 # Progeam for ROCK PAPER SCISSORS Game.
# 0 For ROCK
# 1 For PAPER
# 2 For SCISSORS

import random

users_choice = int(input("enter your choices 0 for rock, 1 for paper and 2 for scissors: "))
comp_choice = random.randint(0,2)

print(f"user choice is: {users_choice}")
print(f"computer choice is: {comp_choice}")

if users_choice ==  comp_choice:
    print(" game is draw try again:")

elif users_choice == 0 and comp_choice == 1:
    print("computer wins")

elif users_choice == 1 and comp_choice == 0:
    print("user wins")

elif users_choice == 0 and comp_choice == 2:
    print("user wins")

elif users_choice == 1 and comp_choice == 2:
    print("computer wins")

elif users_choice == 2 and comp_choice == 1:
    print("computer wins")

elif users_choice == 2 and comp_choice == 0:
    print("computer wins")

else:
    print("invalid input")

    
