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
