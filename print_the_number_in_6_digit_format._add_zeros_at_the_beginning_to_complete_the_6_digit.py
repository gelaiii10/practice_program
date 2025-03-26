#ask the user to input a number between 0 and 1000
num = int(input("enter a number between 0 and 1000: "))
#check if the number is within the valid range
if 0 <= num <= 1000:
    #format the number to 6 digits with leading zeroes
    formatted_number = f"{num:06}"