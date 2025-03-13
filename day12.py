# Modifying Global Scope

enemies = 1


def increase_enemies(enemy):
    # global enemies
    # enemies += 1
    # print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)

print(enemies)
print(f"enemies outside function: {enemies}")


import random

# Setting basic functios and setup for game
game_running = True

difficulty = input(f"Welcome to the number guessing game. Would you like to play easy or hard? type 'h' or 'e'. ")

if difficulty == 'h':
    lives = 5
else:
    lives = 10

random_number = random.randint(1,100)

# Start of primary game logic
#while game is running, continue to get guesses until the game stops runnign
while game_running:
    #first check if we still have enough lives
    if lives > 0:
        guess = int(input("Try to guess the number. "))
        #check their guess
        if guess > random_number:
            lives -= 1
            print("lower", lives)
        elif guess < random_number:
            lives -= 1
            print("higher", lives)
        elif guess == random_number:
            print("you win")
            game_running = False
    else:
        print("your out of lives and you lose. ")
        game_running = False

print(random_number, lives)
