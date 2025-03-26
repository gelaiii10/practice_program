#ask the user to input their full name in incorrect casing
full_name = input("enter your full name in incorrect casing: ")
#reverse the casing of each character
reversed_casing_name = ''.join(char.swapcase() for char in full_name)