import random

my_num = random.randint(0,1)

if my_num == 0:
    print(f"heads")
else:
    print(f"tails")


import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# print(friends[random.randint(0, len(friends)-1)])
print(random.choice(friends))



import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

# Getting the choices from the user and computer
userChoice = options[int(input("choose 0 for rock 1 for paper and 2 for scissors"))]
compChoice = random.choice(options)

# compare the choices
# user  chooses rock logic
# any and all ties
if userChoice == compChoice:
    print(f"you choice {userChoice}\n and the computer chose {compChoice}\n its a draw")

#     user chooses rock computer chooses paper
elif userChoice == options[0] and compChoice == options[1]:
    print(f"you choice {userChoice}\n and the computer chose {compChoice}\n computer wins ")
#     user  chooses rock and  computer  chooses scissors
elif userChoice == options[0] and compChoice == options[2]:
    print(f"you choice {userChoice}\n and the computer chose {compChoice}\n you win ")

#     user chooses paper logic
# user chooses paper comp chooses rock
elif userChoice == options[1] and compChoice == options[0]:
    print(f"you choice {userChoice}\n and cthe computer chose {compChoice}\n you win ")
#     user chooses paper and comp chooses scissors
elif userChoice == options[1] and compChoice == options[0]:
    print(f"you choice {userChoice}\n and cthe computer chose {compChoice}\n computer win ")

#     user  chooses scissors logicgi
# scissors vs rock
elif userChoice == options[2] and compChoice == options[0]:
    print(f"you choice {userChoice}\n and cthe computer chose {compChoice}\n computer win ")
#     scissors vs paper
elif userChoice == options[2] and compChoice == options[1]:
    print(f"you choice {userChoice}\n and cthe computer chose {compChoice}\n you win ")
