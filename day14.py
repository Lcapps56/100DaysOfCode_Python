import random
score = 0
game_running = True
characters = [
    {
        'desc': 'Rihanna, an American singer/songwriter',
        'followers': 500000
    },
    {
        'desc': 'Charlie Puth, a singer-songwriter from Britain',
        'followers': 300000
    },
    {
        'desc': 'David Beckham, an American soccer player',
        'followers': 1000000
    },
    {
        'desc': 'Oliver Tree, a singer-songwriter from America',
        'followers': 150000
    },
    {
        'desc': 'Taylor Swift, a globally renowned American singer-songwriter',
        'followers': 900000
    },
    {
        'desc': 'Cristiano Ronaldo, a Portuguese professional footballer',
        'followers': 1200000
    },
    {
        'desc': 'Ariana Grande, a pop singer and actress from America',
        'followers': 750000
    },
    {
        'desc': 'Elon Musk, an entrepreneur and CEO of Tesla and SpaceX',
        'followers': 1100000
    },
    {
        'desc': 'Zendaya, an American actress and singer',
        'followers': 650000
    },
    {
        'desc': 'Shakira, a Colombian singer and dancer',
        'followers': 850000
    }
]



# Pick a random character for character A
character_A = characters[random.randint(0,9)]

# Pick a random Character for character B
character_B = characters[random.randint(0,9)]
# Ensure that we never are compariung the same character to each other
if character_B == character_A:
    while character_B == character_A:
        character_B = characters[random.randint(0, 9)]

# Print both my characters

while game_running:

    print(character_A, character_B)
    print(f" who do you think has more followers?\n A - {character_A['desc']} \nor \n B - {character_B['desc']}")
    decision = input("Type 'A' or 'B'").lower()

    # if characert A was chose and its correct - let user know and add a pount - rerun loop
    if decision == "a" and character_A['followers'] > character_B['followers']:
        print("A is correct")
        print(f"{character_A['desc']} has {character_A['followers']} followers and {character_B['desc']} has {character_B['followers']}")
        score += 1
        print(score)

        # Choose new character B
        character_B = characters[random.randint(0, 9)]
        # Ensure that we never are compariung the same character to each other
        if character_B == character_A:
            while character_B == character_A:
                character_B = characters[random.randint(0, 9)]

    # if character b was chosen and that is correct - let user know and print score - rerun loop
    elif decision == "b" and character_A['followers'] < character_B['followers']:
        print("B is correct")
        print(f"{character_A['desc']} has {character_A['followers']} followers and {character_B['desc']} has {character_B['followers']}")
        score += 1
        print(score)

        character_A = character_B
        character_B = characters[random.randint(0, 9)]
        # Ensure that we never are compariung the same character to each other
        if character_B == character_A:
            while character_B == character_A:
                character_B = characters[random.randint(0, 9)]
    # if they are incorrect - end game
    else:
        print("incorrect")
        print(f"game over. Your score is {score}")
        game_running = False
        break
