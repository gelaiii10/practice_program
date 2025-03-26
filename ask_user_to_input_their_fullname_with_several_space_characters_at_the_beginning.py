#ask the user to input their fullname with several space
fullname = input("enter your full name: ")
#remove leading spaces using the strip() method
cleaned_fullname = fullname.lstrip()
#print the cleaned full name