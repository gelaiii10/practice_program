#ask user to input their full name
full_name = input("enter your full name: ")
#convert the input into pascal case
pascal_case_name = ''.join(word.capitalize() for word in full_name.split())
#print the full name into pascal case
print(pascal_case_name)