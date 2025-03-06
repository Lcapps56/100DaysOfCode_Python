def greet(name):
    print(f"hello {name}")

greet("Leland")


def calculate_love_score(name1, name2):
    love_score = ""
    counter = 0
    test_words = ["t", "r", "u", "e", "l", "o", "v", "e"]

    # how many times does (letter) appear in (name)
    for letter in name1:
        if letter in test_words:
            counter += 1

    love_score += str(counter)
    for letter in name2:
        if letter in test_words:
            counter += 1

    love_score += str(counter)

    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt( original_text, shift_amount):
    encrypted_message = ""
    for letter in original_text:
        if alphabet.index(letter) + shift_amount >= 25:
            # new index number = how many times can the alphabet len fit into the (shift number plus alphabet)
            my_num = alphabet.index(letter) + shift_amount

            new_index = len(alphabet) % my_num

            encrypted_message += alphabet[new_index]



            # encrypted_message += alphabet[alphabet.index(letter) + shift_amount - 26]
        else:
            encrypted_message += alphabet[alphabet.index(letter) + shift_amount]
        # for every


    print(encrypted_message)



# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


encrypt(text, shift)

TODO-1: Import and print the logo from art.py when the program starts.
from os import error

import art
logo = art.logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            break

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

    again = input("Do you want to play again?").lower()
    if again == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or stop to stop:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)




# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)




