# strings, f string, math operators,  data types

len("Hello")

print("Hello"[-1] )

print(type("string"))

print(type(123))

print(type(True))

print(type(1.2))


print("Number of letters in your name: " + str(len(input("Enter your name"))))

print("My age: " + str(12))

print(int(3 * (3 + 3) / 3 - 3))

bmi = 84 / 1.65 ** 2



print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

people = int(input("How many people to split the bill? "))

amount = (bill*(tip/100))/people


print(f"Each person needs to tip ${amount:.2f}")
