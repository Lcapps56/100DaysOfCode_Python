fruits = ["Apple", "Peach", "Pear"]


for num in range(1, 101):
    if not num % 3  and not num % 5:
        print(f"FizzBuzz")
    elif not num % 3:
        print(f"Fizz")
    elif not num % 5:
        print(f"Buzz")
    else:
        print(num)

        print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_password = []
#
# for char in range(nr_symbols):
#     new_password += random.choices(symbols)
# for char in range(nr_numbers):
#     new_password += random.choice(numbers)
# for char in range(nr_letters):
#     new_password += random.choice(letters)

new_password += random.choices(symbols, k=nr_symbols)
new_password += random.choices(letters, k=nr_letters)
new_password += random.choices(numbers, k=nr_numbers)

random.shuffle(new_password)

print("".join(new_password))