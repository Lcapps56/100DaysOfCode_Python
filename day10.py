def to_capitol(f_name, l_name):
    """This is the docstring for the function"""
    return f_name.upper(), l_name.title()

print(to_capitol("leland", "capps"))

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


# CALCULATOR
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# def calculater():


def calculater():
    running = True
    num1 = float(input("What is your first number? \n"))
    while running:
        operator = str(input("What math function do you want to do? '+', '-', '*', or '/'"))
        num2 = float(input("What is the second number?\n"))
        result = operations[operator](num1, num2)
        print(f"{str(num1)} {operator} {str(num2)} = {result}")

        do_continue = input(f"Would you like to do another operation using {result}? type 'y' or 'n'")

        if do_continue == "n":
            running = False
            calculater()
        else:
            num1 = result


print(calculater())

