student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def convert_grades(scores):

    for grade in scores:
        letter_grade = ""
        if scores[grade] >= 91:
            letter_grade += "A"
        elif 81 <= scores[grade] <= 90:
            letter_grade += "B"
        elif 71 <= scores[grade] <= 80:
            letter_grade += "C"
        else:
            letter_grade += "F"
        scores[grade] = letter_grade

    print(scores)


convert_grades(student_scores)


# Highest Bidder
# TODO-1: Ask the user for input
from operator import is_not

my_bids={}

def calculate_highest(bids):
    # this is the variabel that will keep track of the numbers and what has been the highest number so far
    highest_so_far = 0
    # this will keep track of the string that is associatef with the nuumber. pretty much splitting the dict key:value into variables
    winner = ""
    # go through each key:value in the dict
    for bid in bids:
        # print(type(my_bids[bid]))
        print(type(highest_so_far))
        # go through each key and examine its value. if that bids value is higher than variabel
        if my_bids[bid] > highest_so_far:
            # set that variabel with the value of whatever key we are currently on
            highest_so_far = my_bids[bid]
            # also put that key in the other value
            winner = bid
        print(my_bids[bid])
        print(f"the hgihest was {winner} with a bid of {highest_so_far}")


def get_info():
    is_next = True
    while is_next:
        name = str(input("What is your name?\n"))
        bid = int(input("What is your bid?\n"))

        my_bids[name]=bid

        do_continue = input("Is there another bidder? Yes or no").lower()
        if do_continue == "yes":
            is_next = True
        else:
            is_next = False

        print(my_bids)


get_info()
calculate_highest(my_bids)
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary



