import art
import random
print(art.logo)
game_running = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hit(player_hand):
    player_hand.append(random.choice(cards))
    return player_hand

def is_winner():
    global game_running
    # if the user has exactly 21 or the computer has gone over 21 the user wins
    if sum(user_hand) == 21 or sum(comp_hand) > 21:
        print(f"You win. Your total is {sum(user_hand)} and the computers is {sum(comp_hand)} ")
        game_running = False
        return game_running
    # if the computer has exactly 21 or the user has gone over, the computer wins
    elif sum(comp_hand) == 21 or sum(user_hand) > 21:
        print(f"Computer win. Your total is {sum(user_hand)} and the computers is {sum(comp_hand)} ")
        game_running = False
        return game_running

    # this part should only happen after user hits s (stand)
    elif sum(comp_hand) > sum(user_hand):
        print(f"Computer win. Your total is {sum(user_hand)} and the computers is {sum(comp_hand)} ")
    else:
        print(f"You win. Your total is {sum(user_hand)} and the computers is {sum(comp_hand)} ")


user_hand = random.choices(cards, k=2)
comp_hand = random.choices(cards, k=2)

# check if there is a bust or a 21 on the table
is_winner()

while game_running:
    # init message
    print(f"Your hand has {user_hand} and your total is {sum(user_hand)} ")
    print(f"The computer has at least a {comp_hand[0]}")

    user_decision = input("Would you like to hit or stand? type 'h' or 's' ")
    if user_decision == "h":
        hit(user_hand)
        hit(comp_hand)
        # user_sum = calculate(user_hand)
        # comp_sum = calculate(comp_hand)
        is_winner()
        print(f"Your cards are {user_hand} and your total us {sum(user_hand)} and the computers cards are {comp_hand} with a total of {sum(comp_hand)}")
    else:
        hit(comp_hand)
        # comp_sum = calculate(comp_hand)
        while sum(comp_hand) <= 16:
            print("computer under 16 and is pulling card")
            hit(comp_hand)
            is_winner()
        is_winner()
