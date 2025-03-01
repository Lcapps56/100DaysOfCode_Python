weight = 85
height = 1.85

bmi = weight / (height ** 2)


num1 = int(input("give me a number"))
if (num1 % 2) == 0:
    print("its even")
else:
    print("its odd")


math_grade = float(input("whats your math grade"))
eng_grade = float(input("whats your english gradeÎ"))


if math_grade >= 90:
    if eng_grade >= 90:
        print("yur good at everything")
    else:
        print(f"your good at math but with an english grade of {eng_grade} you need work")
else:
    if eng_grade >= 90:
        print(f"your good at english but your math needs work")

height = int(input("how tall are you"))
price = 0

if height > 160:
    print(f"You can ride! lets see how much you have to pay")
    age = int(input("What is your age?"))
    if age > 18:
        price = 10
    elif age > 12:
        price = 5
    else:
        price = 0
    photo = input(f"do you want a photo?")
    if photo == "yes":
        price = price + 3
    else:
        price = price
    print(f"you pay {price}")
else:
    print("sorry you cant ride")



    print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print(f"damn itll be ight")
        bill = bill
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


    print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

dec1 = input(f"Left or right?\n")

if dec1 != 'left':
    print(f"game over")

dec2 = input("theres a lake. looks like you can swim it. you could also wait for a boat. do you swim or wait?\n")

if dec2 != "wait":
    print("you got ate by a shark")

print(f"you made it to the other side. There are 3 doors. red yellow and blue.")
dec3 = input(f"Whcih door do you go through?\n")

if dec3 == "blue":
    print('eaten by beasts game over')
elif dec3 == "yellow":
    print(f"burned by fire")
elif dec3 == "red":
    print(f"you won")





